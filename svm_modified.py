from sklearn import svm
import csv

train_file = open('trimeedtraining.csv','rb')
train = csv.reader(train_file , delimiter=',')

X=[]
Y=[]

for row in train:
	X=[[float(row[1]),float(row[2]),float(row[3])]]+X
	Y=[row[4]]+Y

train_file.close()

print 'X'
clf = svm.SVC()
clf.fit(X, Y)

test_file = open('test.csv','rb')
test = csv.reader(test_file , delimiter=',')
X=[]
seqId=[]
count=-1
for row in test:
	if(count == -1):
		pass
	else:
		X=[[float(row[1]),float(row[2]),float(row[3])]]+X
		seqId=[row[4]]+seqId
	if (count > 30000):
		break
	count = count+1
test_file.close()

dev=clf.predict(X)

out=zip(dev,seqId)

for row in out:
	print row



