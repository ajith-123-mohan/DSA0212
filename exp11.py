import cv2
import numpy as np

img = cv2.imread('house.jpg')
rows, cols = img.shape[:2]

# Define 4 source points (corners of an object in the image)
pts_src = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])

# Define 4 destination points (where you want them to go)
pts_dst = np.float32([[10, 100], [180, 30], [80, 230], [230, 150]])

# DLT works by finding the homography matrix
M, _ = cv2.findHomography(pts_src, pts_dst)

# Apply the transformation
dst = cv2.warpPerspective(img, M, (cols, rows))

cv2.imshow('DLT Transformation', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()