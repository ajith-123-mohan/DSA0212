import cv2

# Load image in grayscale
img = cv2.imread('house.jpg', 0)

# Sobel XY (dx=1, dy=1)
sobelxy = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)

cv2.imshow('Sobel XY (Combined)', sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()