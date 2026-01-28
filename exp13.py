import cv2

# Load image in grayscale
img = cv2.imread('house.jpg', 0)

# Sobel X-axis (dx=1, dy=0)
# ksize=3 means a 3x3 Sobel filter
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

cv2.imshow('Sobel X-axis', sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()