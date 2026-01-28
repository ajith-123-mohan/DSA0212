import cv2
import numpy as np

# 1. Read the image in Python
# 'img' holds the original color image (BGR format)
img = cv2.imread('house.jpg')

# Check if image loaded successfully
if img is None:
    print("Error: Could not read 'house.jpg'. Please make sure the file exists in the same folder.")
else:
    # 2. Convert Image to Grayscale
    # Color conversion from BGR (Blue-Green-Red) to Gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Convert Image to Blur using Gaussian Blur
    # (7, 7) is the kernel size (must be odd), 0 is sigmaX
    blur = cv2.GaussianBlur(gray, (7, 7), 0)

    # 4. Show outline using Canny function
    # 100 is the lower threshold, 200 is the upper threshold
    edges = cv2.Canny(blur, 100, 200)

    # Define a kernel for morphological operations (5x5 matrix of 1s)
    kernel = np.ones((5, 5), np.uint8)

    # 5. Dilate an Image using Dilate function
    # Dilation adds pixels to the boundaries of objects (makes white regions thicker)
    dilated = cv2.dilate(edges, kernel, iterations=1)

    # 6. Erode an Image using Erode function
    # Erosion removes pixels on object boundaries (makes white regions thinner)
    eroded = cv2.erode(dilated, kernel, iterations=1)

    # --- Displaying Results ---
    cv2.imshow('1. Original Image', img)
    cv2.imshow('2. Grayscale', gray)
    cv2.imshow('3. Gaussian Blur', blur)
    cv2.imshow('4. Canny Edges', edges)
    cv2.imshow('5. Dilated Edges', dilated)
    cv2.imshow('6. Eroded (Restored)', eroded)

    # Wait indefinitely until a key is pressed, then close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()