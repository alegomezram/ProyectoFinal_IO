import cv2
from PIL import Image

img = Image.open("I1.png") 
print (img.histogram())

I1= cv2.imread("I1.png",-1)
print (I1.histogram())