#!/usr/bin/python
import csv
import sys
import re
que_file = open('questions.csv','rb')
que_csv = csv.reader(que_file , delimiter=',')

train_stat_file = open('tr_statistics.csv','rb')
dev_csv = csv.reader(train_stat_file , delimiter=',')

nb_output_file = open('nb_modified_op.csv','rb')
output_csv = csv.reader(nb_output_file , delimiter=',')

que_csv.next()
dev_csv.next()
output_csv.next()

D={}  # dictionary for each device
for row in dev_csv:
	devid = row[0]
	count=int(row[1])
 	D[devid]=count
train_stat_file.close()
	
Q={} 
for que in que_csv:
	qno=que[0]
	devid=que[2]
	Q[qno]=devid
que_file.close()

outlines=["QuestionId,IsTrue\r\n"]
for op in output_csv:	
	qno=op[0]   
	p=op[1]
	if re.match(p,'nan'):
		prob=1.0
	else:
		count=D[Q[qno]]	
		print "count",count
		pr=float(p)
		prob=pr/count
	outline=qno+","+prob.__format__("1.12f")
	print outline
	outlines.append(outline+"\r\n")
nb_output_file.close()
print "writing to nb_modified_csv file"    
out=open("submission_op2.csv","w")
out.writelines(outlines)
out.close()
