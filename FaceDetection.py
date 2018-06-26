
# coding: utf-8

# In[13]:


#######################################----Face Detection----###########################################
#!/usr/bin/python3
import cv2
#import face detection database xml file
faced_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#initialize video capture device
cap=cv2.VideoCapture(0)
while cap.isOpened():
	#read image
	img=cap.read()[1]
	#convert image to grayscale
	grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#set faced_data to detect multiple face or frame
	faces=faced_data.detectMultiScale(grayimg,2,5)
	for (x,y,w,h) in faces :
    		#draw rectangle 
    		cv2.rectangle(img,(x,y),(x+w,y+h),(80,255,90),2)
    		roi_gray=grayimg[y:y+h,x:x+w]
    		roi_color=img[y:y+h,x:x+w]
	#show image
	cv2.imshow("Face Detection",img)
	if cv2.waitKey(1) & 0xff == ord('q'):
    		break
cv2.destroyAllWindows()
#release camera
cap.release()


# In[14]:


#######################################----Eye Detection----###########################################
#!/usr/bin/python3
import cv2
#import eye detection database xml file
eye_data=cv2.CascadeClassifier('haarcascade_eye.xml')
#initialize video capture device
cap=cv2.VideoCapture(0)
while cap.isOpened():
	#read image
	img=cap.read()[1]
	#convert image to grayscale
	grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#set faced_data to detect multiple frames
	eyes=eye_data.detectMultiScale(grayimg,2,5)
	for (x,y,w,h) in eyes :
    		#draw rectangle 
    		cv2.rectangle(img,(x,y),(x+w,y+h),(80,255,90),2)
    		roi_gray=grayimg[y:y+h,x:x+w]
    		roi_color=img[y:y+h,x:x+w]
	#show image
	cv2.imshow("Face Detection",img)
	if cv2.waitKey(1) & 0xff == ord('q'):
    		break
cv2.destroyAllWindows()
cap.release()


#####################################----Face with Eye Detection----#######################################
#!/usr/bin/python3
import cv2
#import eye and face detection database xml file
eye_data=cv2.CascadeClassifier('haarcascade_eye.xml')
faced_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#initialize video capture device
cap=cv2.VideoCapture(0)
while cap.isOpened():
	#read image
	img=cap.read()[1]
	#convert image to grayscale
	grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#set eye_data to detect multiple frames
	eyes=eye_data.detectMultiScale(grayimg,2,5)
	for (x,y,w,h) in eyes :
    		#draw rectangle 
    		cv2.rectangle(img,(x,y),(x+w,y+h),(80,255,90),2)
    		roi_gray=grayimg[y:y+h,x:x+w]
    		roi_color=img[y:y+h,x:x+w]
	#set face_data to detect multiple frames
	faces=faced_data.detectMultiScale(grayimg,2,5)
	for (x,y,w,h) in faces :
    		#draw rectangle 
    		cv2.rectangle(img,(x,y),(x+w,y+h),(80,255,90),2)
    		roi_gray=grayimg[y:y+h,x:x+w]
    		roi_color=img[y:y+h,x:x+w]
	#show image
	cv2.imshow("Face wit Eye Detection",img)
	if cv2.waitKey(1) & 0xff == ord('q'):
    		break
cv2.destroyAllWindows()
cap.release()
