import os
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2

model = torch.hub.load(os.getcwd(), 'custom', source='local', path = 'best.pt', force_reload = True)
img = 'Valid/19.jpg'
gambar = cv2.imread(img)
results = model(img)

cls = results.pandas().xyxy[0]['name'].to_numpy()
conf = results.pandas().xyxy[0]['confidence'].to_numpy()
print(cls)
print(conf)


#2,4,5,8,13,14
