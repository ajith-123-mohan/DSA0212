import cv2
import numpy as np

img = cv2.imread('house.jpg')
# Define 4 corner points of the object in the original image
pts1 = np.float32([[56,65], [368,52], [28,387], [389,390]])
# Define where these 4 points should be in the output (flat rectangle)
pts2 = np.float32([[0,0], [300,0], [0,300], [300,300]])

# Calculate the Perspective Matrix
M = cv2.getPerspectiveTransform(pts1, pts2)
# Apply the transformation (output size is 300x300)
dst = cv2.warpPerspective(img, M, (300, 300))

cv2.imshow('Perspective Transformation', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()