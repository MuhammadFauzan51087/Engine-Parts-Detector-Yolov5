import os
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
model_name='best.pt'
model = torch.hub.load(os.getcwd(), 'custom', source='local', path = model_name, force_reload = True)

img = 'Valid/2.jpg'
results = model(img)

    
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
