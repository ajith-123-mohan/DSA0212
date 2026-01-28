import cv2
import numpy as np

img = cv2.imread('house.jpg')

# 4 Source points (corners in original image)
pts_src = np.array([[141, 131], [480, 159], [493, 630], [64, 601]])
# 4 Destination points (corners in output image)
pts_dst = np.array([[0, 0], [300, 0], [300, 300], [0, 300]])

# Calculate Homography Matrix
h, status = cv2.findHomography(pts_src, pts_dst)

# Warp source image to destination based on homography
dst = cv2.warpPerspective(img, h, (300, 300))

cv2.imshow('Homography Transformation', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()