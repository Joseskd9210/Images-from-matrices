
"""
Jose Fernández Ortiz
"""                       


import numpy as np
import cv2
import os
from math import sqrt
path ='c:\\improc'
os.chdir(path)
image = np.zeros((500,500), 'uint8')
image2 = np.zeros((500,500), 'uint8')
rows, cols = image.shape[:2]

X = cols/2
Y = rows/2

distanceCenter = sqrt(pow(X, 2) + pow(Y, 2))

def distance (x,y):
    return sqrt(pow(abs(x - X), 2) + pow(abs(y - Y), 2))

for i in range(rows):
    for j in range(cols):
        
        image[i,j] = 255 * (distance(i,j)/distanceCenter)

for i in range(rows):
    for j in range(cols):
        
        image2[i,j] = 255 * (distance(i,j)/distanceCenter) * (-1)


cv2.imshow('BlackWhite', image)
cv2.imshow('WhiteBlack', image2)
cv2.waitKey()

cv2.destroyAllWindows()
