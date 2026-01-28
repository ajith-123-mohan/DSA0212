import cv2
import numpy as np

# Load image in grayscale
img = cv2.imread('house.jpg', 0)

# Boundary Kernel (highlights all edges)
# [-1, -1, -1]
# [-1,  8, -1]
# [-1, -1, -1]
kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

# filter2D applies the convolution
boundary = cv2.filter2D(img, -1, kernel)

cv2.imshow('Boundary Detection', boundary)
cv2.waitKey(0)
cv2.destroyAllWindows()