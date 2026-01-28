import cv2

# 1. Load the car detector (Ensure you have the .xml file)
car_cascade = cv2.CascadeClassifier('car.xml') 
cap = cv2.VideoCapture('car.mp4') # Use 0 for live camera

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    # 2. Process frame (Convert to Gray for speed)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 3. Detect cars
    cars = car_cascade.detectMultiScale(gray, 1.1, 2)

    # 4. Draw boxes around detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    cv2.imshow('Vehicle Detection', frame)
    
    if cv2.waitKey(1) == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()