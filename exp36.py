import cv2
img = cv2.imread('house.jpg')
x, y, w, h = cv2.selectROI("Select", img)
crop = img[y:y+h, x:x+w]
cv2.imshow("Extracted", crop)
cv2.waitKey(0)
