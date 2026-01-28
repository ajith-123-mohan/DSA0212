import cv2
import numpy as np

cap = cv2.VideoCapture('Cat.mp4')

while True:
    ret, frame = cap.read()
    if not ret: break # Stop if video ends

    # 4 points of the area to warp -> 4 points of the target square
    pts1 = np.float32([[100,100], [400,100], [100,400], [400,400]])
    pts2 = np.float32([[0,0], [300,0], [0,300], [300,300]])

    # Generate matrix and apply in one go
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (300, 300))

    cv2.imshow('Warped Video', result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()