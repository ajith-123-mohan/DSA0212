import cv2

# Load the image
img = cv2.imread('house.jpg')

# Add text watermark
# (img, text, position, font, scale, color, thickness)
cv2.putText(img, 'PROPERTY OF AI', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

# Save and Show
cv2.imwrite('text_watermarked.jpg', img)
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()