import cv2

img = cv2.imread('house.jpg')

# 1. CROP: img[y1:y2, x1:x2]
roi = img[100:300, 100:300] 

# 2. COPY
crop = roi.copy()

# 3. PASTE: Target area must be the same size (200x200)
img[0:200, 0:200] = crop

cv2.imshow('Crop and Paste', img)
cv2.waitKey(0)
cv2.destroyAllWindows()