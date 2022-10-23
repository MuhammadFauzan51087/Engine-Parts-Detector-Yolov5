import os
import torch
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import cv2

model = torch.hub.load(os.getcwd(), 'custom', source='local', path = 'best.pt', force_reload = True)
img = 'Valid/2.jpg'

results = model(img)
import pandas as pd

Xmin= results.pandas().xyxy[0]

#print(Xmin)
print(Xmin['name'].notna())
#df = pd.DataFrame(Xmin)

#print(results.pandas().xyxy[0])  # img1 predictions (pandas)

#2
