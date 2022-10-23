import os
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
model_name='best.pt'
model = torch.hub.load(os.getcwd(), 'custom', source='local', path = model_name, force_reload = True)
#print(os.getcwd())
#model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)
img = 'Valid/2.jpg'
#cap = cv2.VideoCapture(0)
results = model(img)
print(type(results))
print(results.xyxy[0])  # img1 predictions (tensor)
print(results.pandas().xyxy[0])  # img1 predictions (pandas)
#print(results.parametes)
#print(np.squeeze(results.render()))
#while True:
#    _,frame = img.read()
    
'''
while cap.isOpened():
    ret, frame = cap.read()
    print(type(frame),frame.shape)
    
    # Make detections 
    results = model(frame)
    
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
#results = model(img)
#print(results)
'''
#2
