import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits import mplot3d
import numpy as np
import time
import cv2


xx=np.linspace(-np.pi,np.pi,num=1024)
yy=np.linspace(-np.pi,np.pi,num=1024)
x,y=np.meshgrid(xx,yy)

r=x**2 +y**2
z=(1/r)*np.exp(1j*r)

np.set_printoptions(threshold=np.inf)
phase=np.angle(z)     #wrapped phase
print(phase[512,:])

# # Plot the surface
# fig = plt.figure(1)
# ax = plt.axes(projection='3d')
# surf = ax.plot_surface(x, y, phase,rstride=5, cstride=5,cmap='viridis', edgecolor='none')
# plt.savefig("phasewrap.png")
# plt.imsave("phasewrap2D.png",phase, cmap='gray') 

# #realphase=np.unwrap(phase)/2
# realphase=(np.unwrap(np.unwrap(phase,axis=0), axis=1))
# # Plot the surface
# fig = plt.figure(2)
# ax = plt.axes(projection='3d')
# surf = ax.plot_surface(x, y, realphase,rstride=5, cstride=5,cmap='viridis', edgecolor='none')
# plt.savefig("phaseunwrap.png")
# plt.imsave("phaseunwrap2D.png",realphase, cmap='gray') 