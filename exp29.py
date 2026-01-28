import cv2
import numpy as np

img = cv2.imread('house.jpg', 0)
kernel = np.ones((5,5), np.uint8)

# Apply Gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('Morphological Gradient', gradient)
cv2.waitKey(0)