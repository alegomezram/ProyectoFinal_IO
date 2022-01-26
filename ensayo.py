import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


x=np.array([0,0,0,0,1,1])

lista=np.where(x>0)

y=x
y[lista]=1/x[lista]
print(x,y,lista)

period=1406.4
discont=703.2
print(period)
print(discont)
print(max(discont, period/2))
