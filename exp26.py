import cv2
import numpy as np

img = cv2.imread('house.jpg', 0)
kernel = np.ones((5,5), np.uint8)

# Apply Dilation
dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Dilation', dilation)
cv2.waitKey(0)