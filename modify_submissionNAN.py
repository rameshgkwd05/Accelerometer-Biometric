#!/usr/bin/python
import csv
import sys
import re

nb_output_file = open('nb_random_op.csv','rb')
output_csv = csv.reader(nb_output_file , delimiter=',')

output_csv.next()


outlines=["QuestionId,IsTrue\r\n"]
for op in output_csv:	
	qno=op[0]   
	p=op[1]
	if re.match(p,'nan'):
		prob='0.000000'
	else:
		prob=p
	outline=qno+","+prob
	print outline
	outlines.append(outline+"\r\n")
nb_output_file.close()
print "writing to nb_modified_csv file"    
out=open("submission_op6.csv","w")
out.writelines(outlines)
out.close()
