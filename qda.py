from sklearn.qda import QDA
import numpy as np
import csv


train_file = open('SampledTrainingSet.csv','rb')
train = csv.reader(train_file , delimiter=',')

X=[]
Y=[]
train.next()
for row in train:
	X=[[float(row[1]),float(row[2]),float(row[3])]]+X
	Y=[row[4]]+Y

train_file.close()

clf = QDA()
clf.fit(X, Y)


test_file = open('test.csv','rb')
test = csv.reader(test_file , delimiter=',')
X=[]
seqId=[]
count=0
skip = 10
for row in test:
	if(count == 0):
		pass
	elif(count % 10 == 0):
		X=[[float(row[1]),float(row[2]),float(row[3])]]+X
		seqId=[row[4]]+seqId
	else:
		pass
	if(count > 30000):
		break
	count = count+1
test_file.close()

dev=clf.predict_log_proba(X)
classes1=clf.classes
out=zip(dev,seqId)
print classes1
for row in out:
	print row
