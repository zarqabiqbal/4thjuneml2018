#!/usr/bin/env python3
from urllib.request import Request, urlopen

values = """
  {
    "image": "https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&cs=tinysrgb&h=650&w=940", 
    "subject_id": "Guava",
    "gallery_name": "MyGallery"
  }
"""
values=bytes(values, 'utf-8')
headers = {
  'Content-Type': 'application/json',
  'app_id': 'app-id',
  'app_key': 'app-key'
}
request = Request('https://api.kairos.com/enroll', data=values, headers=headers)
print(request)
response_body = urlopen(request).read()
print (response_body)

