import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits import mplot3d
import numpy as np
import time
import cv2
from PIL import Image

xx=np.linspace(-np.pi,np.pi,num=2048)
yy=np.linspace(-np.pi,np.pi,num=2048)
x,y=np.meshgrid(xx,yy)

im = Image.open('MembranePhase.tif') 


# Plot the surface
fig = plt.figure(1)
# ax = plt.axes(projection='3d')
# surf = ax.plot_surface(x, y, im,rstride=5, cstride=5,cmap='viridis', edgecolor='none')
# plt.savefig("phasewraptest2.png")
plt.imsave("phasewrap2Dtest2.png",im, cmap='gray') 

# #realphase=np.unwrap(phase)/2
# realphase=(np.unwrap(np.unwrap(phase,axis=0), axis=1))
# # Plot the surface
# fig = plt.figure(2)
# ax = plt.axes(projection='3d')
# surf = ax.plot_surface(x, y, realphase,rstride=5, cstride=5,cmap='viridis', edgecolor='none')
# plt.savefig("phaseunwraptest2.png")
# plt.imsave("phaseunwrap2Dtest2.png",realphase, cmap='gray') 