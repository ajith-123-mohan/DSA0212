import cv2
import numpy as np

img = cv2.imread('house.jpg')

# Laplacian Mask with Diagonal Neighbors (Negative Center -8)
# [ 1,  1,  1]
# [ 1, -8,  1]
# [ 1,  1,  1]
kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

# Apply the filter
laplacian = cv2.filter2D(img, -1, kernel)

# Subtract Laplacian from original to get the sharpened result
sharpened = cv2.subtract(img, laplacian)

cv2.imshow('Sharpened (8-Neighbor)', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()