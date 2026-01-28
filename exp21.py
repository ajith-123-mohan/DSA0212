import cv2
import numpy as np

img = cv2.imread('house.jpg', 0) # Load as Grayscale

# 1. Calculate Gradients in X and Y directions
grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# 2. Combine them to get the Magnitude (the Gradient Mask)
gradient_mask = cv2.sqrt(cv2.pow(grad_x, 2) + cv2.pow(grad_y, 2))
gradient_mask = np.uint8(np.absolute(gradient_mask))

# 3. Add the mask to the original image
sharpened = cv2.add(img, gradient_mask)

cv2.imshow('Gradient Sharpening', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()