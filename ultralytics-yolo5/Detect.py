import os
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2

model = torch.hub.load(os.getcwd(), 'custom', source='local', path = 'best.pt', force_reload = True)
img = 'Valid/2.jpg'
gambar = cv2.imread(img)
results = model(img)

Xmin= results.pandas().xyxy[0]['name'].to_numpy()

print(Xmin)
#df = pd.DataFrame(Xmin)

#print(results.pandas().xyxy[0])  # img1 predictions (pandas)

#2
