#!/usr/bin/python
import os,csv,sys,re
import numpy as np
from numpy import matrix
import random

test_file = open('test.csv','rb')		#persistent file handle
test_csv = csv.reader(test_file , delimiter=',') 
test_csv.next()  # skipping header row

# gettestdata(_) function will get test cases matching to particular sequence ids
def gettestdata(seqid):
	flag = 0
	xyz=[]
	#start from previous stop point(break-pt)
	for row in test_csv:
		if (int(row[-1]) == seqid):
			xrow= map(float,row[1:-1])
			xyz.append(xrow)
			flag = 1		
		else:
			if (flag == 1):
				break
			else:
				pass
	
	return xyz


# START

train_stat_file = open('tr_statistics.csv','rb')
train_stat_csv = csv.reader(train_stat_file , delimiter=',')

DEVdict={}  # dictionary for each device
train_stat_csv.next() # skipping first line
for row in train_stat_csv:
    count=int(row[1])
    mux=float(row[2])
    vx= float(row[3])
    muy=float(row[4])
    vy= float(row[5])
    muz=float(row[6])
    vz= float(row[7])
    
    mu=np.matrix([[mux],[muy],[muz]])				# creating mmatrix
    sig=np.matrix([[vx,0.0,0.0],[0.0,vy,0.0],[0.0,0.0,vz]])	# creating matrix form
    multiplier=1/np.sqrt((2.0*np.pi)**3.0*vx*vy*vz)		#taking 3rd power as there are 3 dimensions
    isig=sigma.I						# taking inverse
    
    DEVdict[row[0]]=(row[0],multiplier,isig,mu,count)		# storing into device dictionary
								
# Model Created (all parameters are ready)
train_stat_file.close()   
print "All parameters are available....waiting for test data.." 



#----Testing...(Deploying model)...............................

que_file = open('questions.csv','rb')
que_csv = csv.reader(que_file , delimiter=',')

print que_csv.next()
outlines=["QuestionId,IsTrue\r\n"]
for cols in que_csv:
    seqid = int(cols[1])
    testdata = gettestdata(seqid)
    
    device=DEVdict[cols[2]]
    multiplier=device[1]
    isig=device[2]
    mu=device[3]
    count=device[4]
        
    p=0.0
    IDX=random.sample(testdata,  30)             # instead of taking all test data (taking random 30 samples from 300 test samples 
                                                 # of particular sequence ID

    for row in testdata:
    	x1=float(row[0])
        x2=float(row[1])
        x3=float(row[2])
            
	X=np.matrix([[x1],[x2],[x3]])
            
	prob= multiplier*np.exp(-0.5*((X-mu).T*isig*(X-mu)))
        p=p+prob.item(0,0)

    p=p*count 			# multiplying with class prior
    if p<0.0000001:		# zeroing very low probability value
        p=0.0
    outline=str(cols[0])+","+p.__format__("1.9f")
    outlines.append(outline+"\r\n")

que_file.close()  
test_file.close()
print "writing to nb_modified_csv file"    
out=open("nb_modified_op.csv","w")
out.writelines(outlines)
out.close()
