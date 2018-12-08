import csv
data=[]
import numpy as np
import cv2
import os
import h5py
import tables

def conv(a):
	l=a.split()
	#print(type(l[0]))
	b=l[0]
	c=b[1:len(b)-1]
	d=l[1]
	e=d[0:len(d)-1]
	l1=[]
	l1.append(int(c))
	l1.append(int(c))
	#print(l1)
	return l1









with open('E:\\CV\\Project\\MSU_8_Class\\test_sift_locations.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
    	your_list = list(row)
    	data.append(your_list)
print(len(data))
path='E:\\CV\\Project\\MSU_8_Class\\Test\\'
features=[]
labels=[]
fcount=0
rcount=0
data1=[]
for i in range(0,len(data)):
	a=data[i][0]
	if a[2]=='f':
		if fcount<=1000:
			data1.append(data[i])
			fcount=fcount+1
	elif a[2]=='r':
		if rcount<=600:
			data1.append(data[i])
			rcount=rcount+1
	if fcount>=1000 and rcount>=600:
		break
fcountf=0
rcountf=0
with open('E:\\CV\\Project\\MSU_8_Class\\test_patches_labels.csv', 'w') as f:
	count=0
	for i in range(0,len(data1)):
		print(i)
		#print(type(data[i]))
		a=data1[i]
		#print(a[3:].split())
		for j in range(2,len(a)):
			a[j]=conv(a[j])
		if len(a)>2:
			p=a[0]
			p=p[2:len(p)-2]
			q=a[1]
			q=int(q[1:len(q)-1])
			if p[0]=='r':
				count=count+1
				t=1
			else:
				t=0
				#fcountf=fcountf+1
			img=cv2.imread(os.path.join(path,p))
			##print(p)
			m,n,r=np.shape(img)
			for j in range(2,len(a)):
				l=a[j]
				p1=l[0]
				q1=int(l[1])
				#print(type(p1),type(q1),type(m),type(n))
				if (p1>46 and p1<(m-48)) and (q1>46 and q1<(n-48)):
					img1=img[p1-47:p1+49,q1-47:q1+49]
					if t==0:
						if fcountf<=1000:
							features.append(img1)
							labels.append(q)
							fcountf=fcountf+1
					else:
						if rcountf<=750:
							features.append(img1)
							labels.append(q)
							rcountf=rcountf+1

			
#print(features)
#print(labels)
print(len(features))
hf = h5py.File('test_data.h5', 'w')
train_features=hf.create_dataset('test_dataset_1', data=features)
train_labels=hf.create_dataset('test_dataset_2', data=labels)
hf.close()


#########  Reading from the file #########

#hf = h5py.File('train_data.h5', 'r')
#print(hf.keys())
#n1 = hf.get('dataset_1')
#n1 = np.array(n1)
#print(np.shape(n1))