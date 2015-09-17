import csv

f = open('train.csv','rb')
f1 = open('trimeedtraining.csv','w+')
fc = csv.reader(f,delimiter=',')
fw = csv.writer(f1,delimiter=',')
f2 = open('train.csv','rb')
fc1 = csv.reader(f2,delimiter=',')
Dics={}
Dics1={}
Dics2={}
dics=[]
count=0

for row in fc1:
	if (row[4] not in Dics1):
		Dics1[row[4]] = 1
	else:    
		Dics1[row[4]]=Dics1[row[4]]+1
f2.close();
for key in Dics1:
	if(Dics1[key] >= 1000):
		Dics[key] = (Dics1[key]/1000)
		Dics2[key] = 1
	else:
		Dics[key] = 1000/Dics1[key]
		Dics2[key] = 0
Dics["Device"]=0
#for index in Dics:
#	print index+'   '+str(Dics[index])+'  '+str(Dics1[index])
count1=0
count2=0
xm=0
ym=0
zm=0
prev=""
for row in fc:
	#if (row[4] not in Dics):
	#	Dics[row[4]] = 1
		#dics = [row[1],row[2],row[3],row[4]]+dics
		#print row[1]+","+row[2]+","+row[3]+","+row[4]+"\r\n"
	#	fw.writerow(row)
	#else:    
	#	if (Dics[row[4]]<100):
	#		#Dics[row[4]]=Dics[row[4]]+1
	#		dics = [row[1],row[2],row[3],row[4]]+dics
	#		fw.writerow(row)
			#print row[1]+","+row[2]+","+row[3]+","+row[4]+"\r\n"
	#	Dics[row[4]]=Dics[row[4]]+1
	if(prev != row[4]):
		count2=0
		xm=0
		ym=0
		zm=0
		prev=row[4]
	if(int(Dics2[row[4]]) == 1):
		#if(count1 < Dics1[row[4]]):
		if(count2 < Dics[row[4]]):
			xm=xm+float(row[1])
			ym=ym+float(row[2])
			zm=zm+float(row[3])
			count2=count2+1
		elif (count2 == Dics[row[4]]):
			xm=xm+float(row[1])
			ym=ym+float(row[2])
			zm=zm+float(row[3])
			fw.writerow([row[0],xm/1000,ym/1000,zm/1000,row[4]])
			xm=0
			ym=0
			zm=0
			count2=0
		#count1=count+1
		#elif(count1==Dics[row[4]]):
			#xm=float(row[1])
			#ym=float(row[2])
			#zm=float(row[3])
			#count1=1
			#count2=1
	elif(int(Dics2[row[4]])==0):
		for i in range(1,int(Dics[row[4]])):
			fw.writerow(row)
f.close();
f2.close();
