from ultralytics import YOLO
import cv2
model = YOLO('yolov8n.pt') 
results = model.predict('watch.jpg')
res_plotted = results[0].plot()
cv2.imshow("Detected Watch", res_plotted)
cv2.waitKey(0)