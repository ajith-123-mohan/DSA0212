import cv2

cap = cv2.VideoCapture('Cat.mp4')
frames = []

# Store all frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    frames.append(frame)
cap.release()

# Play backward
for f in reversed(frames):
    # Quick resize to fit screen (800px wide)
    h, w = f.shape[:2]
    out = cv2.resize(f, (800, int(h * (800 / w))))
    
    cv2.imshow('Reverse', out)
    if cv2.waitKey(30) == ord('q'): break

cv2.destroyAllWindows()