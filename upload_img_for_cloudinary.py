from config import *
import cloudinary
import cloudinary.uploader
import glob
import csv
import os
import sys

'''
Script to upload all images in the 
root_dir = './new_images' to cloudinary
and get the URL of this images saved in 
url_list.csv
'''

cloudinary.config( 
  cloud_name = config["cloud_name"], 
  api_key = config["api_key"], 
  api_secret = config["api_secret"],
)

i=0
url_list = []
root_dir = os.path.join(os.getcwd(), 'new_images')


for filename in glob.iglob(root_dir + '**/*.jpg', recursive=True):
  i += 1
  try: 
    res_cloud = cloudinary.uploader.upload(filename, public_id='img%d'%(i))
  except:
    print("Unexpected error:", sys.exc_info()[0])

  print(filename)
  url_img = res_cloud['url']
  print(url_img)
  url_list.append(['%s'%(url_img)])

with open('url_list.csv', 'w') as file:    
  writer = csv.writer(file)
  writer.writerow(['url'])
  writer.writerows(url_list)

