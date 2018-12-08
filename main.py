import keras
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
from sklearn.feature_extraction import image
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json




face_cascade = cv2.CascadeClassifier("E:\\Softwares\\Anaconda\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier('E:\\Softwares\\Anaconda\\Library\\etc\\haarcascades\\haarcascade_eye.xml')

img=cv2.imread('E:\\CV\\Project\\MSU_8_Class\\WIN_20180501_15_15_29_Pro.jpg')
cv2.imshow('input',img)
cv2.waitKey(0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
	sub_face = img[y:y+h, x:x+w]
	cv2.imshow('img',sub_face)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	convface=cv2.cvtColor(sub_face,cv2.COLOR_BGR2HSV)
	sift = cv2.xfeatures2d.SIFT_create()
	kp1, des1 = sift.detectAndCompute(convface,None)
m,n,q=np.shape(img)
print(kp1)
data=[]
for i in range(0,len(kp1)):
	p1=int(kp1[i].pt[0])
	q1=int(kp1[i].pt[1])
	if (p1>46 and p1<(m-48)) and (q1>46 and q1<(n-48)):
		img1=img[p1-47:p1+49,q1-47:q1+49]
		data.append(img1)
#data = np.expand_dims(data, axis=0)


#print(np.shape(data2))
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model_weights.h5")
print("Loaded model from disk")
faccu=0
raccu=0
for i in range(0,len(data)):
	data2=data[i]
	data2 = np.expand_dims(data2, axis=0)
	v=loaded_model.predict(data2)
	a=v[0]
	faccu=faccu+a[0]
	raccu=raccu+a[1]
print("The probability  of  fake image: "+str(faccu/len(data)))
print("The probability of original image: "+str(raccu/len(data)))