from square_function import crop_img
import glob
import os

''' The images are named as 'img' + a number,
    do it to resize a bounch of images
 '''

# path of the a bunch of images to resize
images_path = os.path.join(os.getcwd(), 'images')
i = 0

#new path of the new images
os.mkdir('new_images')

for filename in glob.iglob(images_path + '**/*.jpg', recursive=True):
    i += 1
    crop_img(filename, new_filename="img%d.jpg"%(i))
