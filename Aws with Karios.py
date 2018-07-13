#!/usr/bin/env python3
from urllib.request import Request, urlopen
import cv2
import os
import random

cap=cv2.VideoCapture(0)
while cap.isOpened():
    status,img=cap.read()
    cv2.imshow("Press C for 2 sec to capture the photo",img)
    if cv2.waitKey(2) & 0xff==ord('q'):
        break
    if  cv2.waitKey(1) & 0xff==ord('c'):
        cv2.imshow("Capture Image",img)
        num=str(random.random())[2:6]
        print(num)
        cv2.imwrite("./images/Image"+num+".jpg",img)
        result=os.system('sshpass -p yourpass scp ./images/Image'+num+'.jpg yourusername@yourip:')
        print("Image Succesfully send")
        url="http://54.88.33.184/images/Image"+num+".jpg"
        print(url)
        values = '''
       	{
        "image": "'''+url+'''", 
        "subject_id": "Zarqab",
        "gallery_name": "MyGallery"
        }'''
        values=bytes(values, 'utf-8')
        print(values)
        headers = {
        'Content-Type': 'application/json',
        'app_id': 'app-id',
        'app_key': 'app-key'
        }
        request = Request('https://api.kairos.com/enroll', data=values, headers=headers)
        response_body = urlopen(request).read()
        print response_body
cv2.destroyAllWindows()
cap.release()
