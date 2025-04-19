import torch
import matplotlib.pyplot as plt
import numpy as np
import cv2

model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # Default: yolov5s

cap = cv2.VideoCapture(0)  # 'V' in VideoCapture should be uppercase
while cap.isOpened():
    ret, frame = cap.read()
    
    result = model(frame)
    if not ret:  # Good practice to check if frame was successfully read
        break

    cv2.imshow('YOLO', np.squeeze(result.render()))

    if cv2.waitKey(10) & 0xFF == ord('q'):  # 'waitKey' not 'waitkey'
        break

cap.release()
cv2.destroyAllWindows()
