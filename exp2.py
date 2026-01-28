import cv2

# Load the video file
cap = cv2.VideoCapture('Cat.mp4')

# 1 = Fast Motion (low delay), 100 = Slow Motion (high delay) 
speed_delay = 1 

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Video Processing', frame)

    # Press 'q' to exit
    if cv2.waitKey(speed_delay) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()