
"""
Jose Fernández Ortiz
"""
import numpy as np
import cv2
import os
from math import sqrt
path ='c:\\improc'
os.chdir(path)
image = np.zeros((500,500,3), 'uint8')

image[:,:,2] = 255 #Set to Red

rows, cols = image.shape[:2]

X = cols/2
Y = rows/2

for j in range(cols):
    image[:,j,1] = float(j)/(cols - 1) * 255
    image[:,j,2] = float(j)/(cols - 1) * 255 * -1

cv2.imshow('GreenRed', image)
cv2.waitKey()

cv2.destroyAllWindows()
