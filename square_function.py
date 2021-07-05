import cv2
import numpy as np
import os

'''
Script to crop an image in a square size,
using the shorter side of the pic
'''


def crop_img(filename, new_filename):
	img = cv2.imread(filename)
	rows, cols, _ = img.shape

	mid_rows = int(rows / 2)
	mid_cols = int(cols / 2)

	if rows < cols :
		cut_square = img[0:rows, mid_cols-mid_rows:mid_cols+mid_rows]
	else:
		cut_square = img[mid_rows-mid_cols:mid_rows+mid_cols, 0:cols]

	# Path for the new and squared images 
	new_images_path = os.path.join(os.getcwd(), 'new_images')

	cv2.imwrite(os.path.join(new_images_path, new_filename), cut_square)
