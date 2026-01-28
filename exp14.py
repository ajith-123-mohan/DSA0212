import cv2

# Load image in grayscale
img = cv2.imread('house.jpg', 0)

# Sobel Y-axis (dx=0, dy=1)
# ksize=3 is the standard filter size
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

cv2.imshow('Sobel Y-axis', sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()