import cv2

img = cv2.imread('house.jpg')

# 1. Create a blurred version
blur = cv2.GaussianBlur(img, (3, 3), 0)

# 2. High-Boost: Result = (A * Original) - Blurred
# Here we use A = 2 (standard high boost)
# Formula: 2.5 * Original - 1.5 * Blurred
high_boost = cv2.addWeighted(img, 2.5, blur, -1.5, 0)

cv2.imshow('High-Boost Sharpening', high_boost)
cv2.waitKey(0)
cv2.destroyAllWindows()