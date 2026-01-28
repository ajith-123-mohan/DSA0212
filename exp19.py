import cv2

img = cv2.imread('house.jpg')

# 1. Blur the image (Create the "Unsharp" version)
blur = cv2.GaussianBlur(img, (5, 5), 1.0)

# 2. Subtract blur from original to get the "Mask" (the details)
mask = cv2.subtract(img, blur)

# 3. Add the mask back to the original image
sharpened = cv2.add(img, mask)

cv2.imshow('Unsharp Masking', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()