#!/usr/bin/python


# script for creating mean and variance for particular class(device ID)
# storing it in tr_statistics.csv file for later use

import csv
import sys
import numpy as np
import pickle


# Sorting device ids
def getsortedids():
	device_file = open('device_ids.csv','rb')
	device_csv = csv.reader(device_file , delimiter=',')
	dids={}
	for row in device_csv:
		devid=int(row[0])
		dids[devid]=devid	
	
	devids=dids.keys()
	devids.sort()
	device_file.close()
	return devids

train_file = open('train.csv','rb')
train_csv = csv.reader(train_file , delimiter=',')
print train_csv.next()

def getstatisticsfordev(devid):
	flag = 0
	xyz=[]
	
	
	for row in train_csv:
		if (int(row[-1]) == devid):
			xrow= map(float,row[1:-1])
			xyz.append(xrow)
			flag = 1		
		else:
			if (flag == 1):
				break
			else:
				pass


	print "writing to csv file.."
	count=len(xyz)
	x=[]
	y=[]
	z=[]
	for rec in xyz:
		x.append(rec[0])
		y.append(rec[1])
		z.append(rec[2])

	mux=np.mean(x)
	muy=np.mean(y)
	muz=np.mean(z)

	varx=np.var(x)
	vary=np.var(y)
	varz=np.var(z)

	outlines=[""]
	outline=str(seqid)+","+str(count)+","+str(mux)+","+str(muy)+","+str(muz)+","+str(varx)+","+str(vary)+","+str(varz)
	print outline
	outlines.append(outline+"\r\n")

	out=open("tr_statistics.csv","a+")
	out.writelines(outlines)
	out.close()

#devids=getsortedids()
#devidop=open('storage/devicesids.pkl','wb')
#pickle.dump(devids,devidop)

#devidinp=open('storage/devicesids.pkl','rb')
#devids=pickle.load(devidinp)
print devids

for row in devids[321:]:
	devid=int(row)
	print "\n",count
	count=count+1
	getstatisticsfordev(devid)

train_file.close()
	
print "Thank you!"
