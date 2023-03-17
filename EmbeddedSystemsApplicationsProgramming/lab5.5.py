import numpy
import PIL
import math
import time
import numpy as np
import cv2
import matplotlib as plt
import io

image=cv2.imread('test.jpg',0)

window_name = 'Edge AI- Tiny Yolo'

cv2.imshow(window_name, image)
raw_key = cv2.waitKey(1000)

rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

def make_square(image,upper_left,size,colour):
	

for x in range (0,240):
	for y in range (0,320):
		r,g,b=rgb[x,y]
		if r>g and r>b and r>128:
			image[x,y]=255,0,0

for x in range (120,127):
	for y in range (64,71):
		image[x,y]=255,168,0

window_name2 = 'Edge AI- Tiny Yolo2'
cv2.imshow(window_name2, image)
raw_key = cv2.waitKey(20000)
