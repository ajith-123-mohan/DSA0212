import cv2
import numpy as np

img = cv2.imread('house.jpg')

# Laplacian Mask with Negative Center
# [ 0,  1,  0]
# [ 1, -4,  1]
# [ 0,  1,  0]
kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

# Apply filter and subtract from original to sharpen
laplacian = cv2.filter2D(img, -1, kernel)
sharpened = cv2.subtract(img, laplacian)

cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()