import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits import mplot3d
import numpy as np
import time
import cv2

w_length=0.633 #um

xx=np.linspace(-np.pi,np.pi,num=1024)
yy=np.linspace(-np.pi,np.pi,num=1024)
x,y=np.meshgrid(xx,yy)

r=x**2 +y**2
k=2*np.pi/w_length
z=(1/r)*np.exp(1j*r)

phase=np.angle(z)     #wrapped phase

# Plot the surface
fig = plt.figure()
ax = plt.axes(projection='3d')
surf = ax.plot_surface(x, y, phase,rstride=4, cstride=4,cmap='viridis', edgecolor='none')

#Figures
plt.savefig("phasewrap.png")
#plt.imsave("phasewrap.png",surf) 