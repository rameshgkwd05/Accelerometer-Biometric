import csv


f = open('train.csv','rb')
fc = csv.reader(f,delimiter=',')
Dics={}

for row in fc:
	if (row[4] not in Dics):
		Dics[row[4]] = 1
	else:    
		Dics[row[4]]=Dics[row[4]]+1
        

for index in Dics:
	print index+'   '+str(Dics[index])
