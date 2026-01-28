import cv2

# Load image
img = cv2.imread('house.jpg')

# Canny Edge Detection (100 and 200 are the min/max thresholds)
edges = cv2.Canny(img, 100, 200)

cv2.imshow('Original', img)
cv2.imshow('Canny Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()