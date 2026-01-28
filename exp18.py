import cv2
import numpy as np

img = cv2.imread('house.jpg')

# Positive Center Mask (+4)
# [ 0, -1,  0]
# [-1,  4, -1]
# [ 0, -1,  0]
kernel = np.array([[0, -1, 0], 
                   [-1, 4, -1], 
                   [0, -1, 0]])

# Apply the mask
laplacian = cv2.filter2D(img, -1, kernel)

# For positive center, we ADD to the original image
sharpened = cv2.add(img, laplacian)

cv2.imshow('Sharpened (Positive Center)', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()