from sklearn.svm import SVC
import numpy as np
import csv
import sys
import re




test_file = open('test.csv','rb')		#persistent file handle
test_csv = csv.reader(test_file , delimiter=',') 
test_csv.next()  # skipping header row

# gettestdata(_) function will get test cases matching to particular sequence ids
def gettestdata(seqid):
	flag = 0
	xyz=[]
	count=0
	#start from previous stop point(break-pt)
	for row in test_csv:
		if (count % 10 !=0):
			pass
		elif (int(row[-1]) == seqid):
			xrow= map(float,row[1:-1])
			xyz.append(xrow)
			flag = 1		
		else:
			if (flag == 1):
				break
			else:
				pass
		count = count +1
	return xyz


# START

train_stat_file = open('tr_statistics.csv','rb')
train_stat_csv = csv.reader(train_stat_file , delimiter=',')

train_stat_csv.next()
X=[]
Y=[]
devcount={}
for row in train_stat_csv:
    count=int(row[1])
    x=float(row[2])
    y=float(row[4])
    z=float(row[6])
    xyz=[x,y,z]
    X.append(xyz)
    Y.append(int(row[0]))
    devcount[int(row[0])]=count
train_stat_file.close()   

Xt=np.array(X)
yt=np.array(Y) 
# Model training start

clf = SVC(probability=True)
clf.fit(Xt, yt) 
C=clf.label_
print "Model Ready...waiting for test data"
que_file = open('questions.csv','rb')
que_csv = csv.reader(que_file , delimiter=',')

print que_csv.next()
outlines=["QuestionId,IsTrue\r\n"]
for cols in que_csv:
    print "Qno",cols[0]
    seqid = int(cols[1])
    devid = int(cols[2])	
    testdata = gettestdata(seqid)

    pid=0
    for i in range(len(C)):
	if (devid==C[i]):
		pid=i
	else:
		pass	

    p=0.0
    for row in testdata:
        x1=float(row[0])
        x2=float(row[1])
        x3=float(row[2])
	
	X=[x,y,z]  
	# Crucial Part
	
	PredArr=clf.predict_proba(X)
        prob=PredArr[0][pid]
	p=p+prob

    p=p*devcount[devid]
    
    if p<0.0000001:
        p=0.0
    if re.match('nan',str(p)):
	p=0.0
    outline=str(cols[0])+","+p.__format__("1.12f")
    print outline	
    outlines.append(outline+"\r\n")

que_file.close()  
test_file.close()
print "writing to svm_op.csv file"    
out=open("svm_op.csv","w")
out.writelines(outlines)
out.close()
    
