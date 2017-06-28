
"""
Jose Fernández Ortiz
"""

import numpy as np
import cv2
import os
from math import sqrt
path ='c:\\improc'
os.chdir(path)
image = np.zeros((500,1000), 'uint8')

image2 = image.copy()
image2[:,:] = 1
image2 *= 255

rows, cols = image2.shape[:2]

X = cols/2
Y = rows/2

for j in range(cols):
    image2[:,j] = abs(float(j) - X)/(cols) * 255 * -1

cv2.imshow('BlackWhite', image2)
cv2.waitKey()

cv2.destroyAllWindows()
