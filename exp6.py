import cv2
import numpy as np

# Load the image
img = cv2.imread('house.jpg')

if img is None:
    print("Error: house.jpg not found.")
else:
    # Get image dimensions (Height, Width)
    rows, cols = img.shape[:2]

    # Create the Translation Matrix [cite: 32]
    # [[1, 0, tx], [0, 1, ty]]
    # tx = 100 (move right 100 pixels)
    # ty = 50  (move down 50 pixels)
    M = np.float32([[1, 0, 100], [0, 1, 50]])

    # Apply the shift
    moved_img = cv2.warpAffine(img, M, (cols, rows))

    # Display
    cv2.imshow('Original', img)
    cv2.imshow('Moved (Translated)', moved_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()