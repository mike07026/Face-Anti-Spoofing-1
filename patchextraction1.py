import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
from sklearn.feature_extraction import image
import csv
face_cascade = cv2.CascadeClassifier("E:\\Softwares\\Anaconda\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier('E:\\Softwares\\Anaconda\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')

def points(img,file,count):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	if len(faces)==0:
		data=[]
		data.append([file])
		if file[0]=='f':
			data.append([0])
		else:
			data.append([1])
		return data
	for (x,y,w,h) in faces:
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		sub_face = img[y:y+h, x:x+w]
		convface=cv2.cvtColor(sub_face,cv2.COLOR_BGR2HSV)
		sift = cv2.xfeatures2d.SIFT_create()
		kp1, des1 = sift.detectAndCompute(convface,None)
		img=cv2.drawKeypoints(convface,kp1,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

		data=[]
		data.append([file])
		if file[0]=='f':
			data.append([0])
		else:
			data.append([1])
			#myFile = open('E:\\CV\\Project\\MSU_8_Class\\train_sift_locations.csv', 'w')
		for i in range(0,len(kp1)):
			a=[]
			a.append(int(kp1[i].pt[0]))
			a.append(int(kp1[i].pt[1]))
			data.append(a)
		if count==686:
			print(kp1)
			print(des1)
		return data






path='E:\\CV\\Project\\MSU_8_Class\\Test'
data1=[]
count=0
#print(data1)
with open('E:\\CV\\Project\\MSU_8_Class\\test_sift_locations.csv', "w") as csv_file:
	for file in os.listdir(path):
		img=cv2.imread(os.path.join(path,file))
		data=points(img,file,count)
		count=count+1
		print(count)
		writer = csv.writer(csv_file,lineterminator = '\n')
		writer.writerow(data)