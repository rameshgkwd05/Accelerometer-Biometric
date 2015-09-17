from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import csv
# we reduce the training data by taking the mean of consecutive samples of same device
train_file = open('trim.csv','rb')
train = csv.reader(train_file , delimiter=',')

X=[]
Y=[]
count = 0
train.next()
for row in train:
	if(count > 300000):               # When we increase the training data the time of training data increase exponentially
		break
	count =count+1
	X=[[float(row[1]),float(row[2]),float(row[3])]]+X
	Y=[row[4]]+Y

train_file.close()


neigh = KNeighborsClassifier(n_neighbors=100)
neigh.fit(X, Y)                           # Fit the training data   


test_file = open('test.csv','rb')
test = csv.reader(test_file , delimiter=',')
X=[]
seqId=[]
count=0
skip = 30
test.next()
for row in test:
	if(count == 0):
		pass
	elif(count % 20 == 0):           # We use only some fraction of test data it doesn't effect much
		X=[[float(row[1]),float(row[2]),float(row[3])]]+X
		seqId=[row[4]]+seqId
	else:
		pass
	count = count+1
test_file.close()

out=neigh.predict_proba(X)            # Now we predict the probability of training data
for x in out:
	print x

