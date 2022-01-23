import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits import mplot3d
import numpy as np
import time
import cv2

#Functions

def unwraping(phase):

	#phase unwrapping

	absolutephase=(np.unwrap(np.unwrap(phase,axis=0), axis=1))

	return absolutephase


def 3D(phaseobj,phaseref,l,d,f):

	#Depth information acquisition

	deltaph=phaseobj-phaseref   #phase difference

	z=(l/d)*(deltaph)  #option1

	z=(l*deltaph)/(deltaph+(2*np.pi*d*f))  #option2

	z=z0+c0*(deltaph)   #option3

	return z


#Import pictures of object
I1= cv2.imread("I1.png",0)  #Intensity of fringe pattern with phase shift=-2pi/3
I2= cv2.imread("I2.png",0)  #Intensity of fringe pattern with phase shift=0
I3= cv2.imread("I3.png",0)  #Intensity of fringe pattern with phase shift=+2pi/3

#Import pictures of reference plane
I1r= cv2.imread("I1r.png",0)  #Intensity of fringe pattern with phase shift=-2pi/3
I2r= cv2.imread("I2r.png",0)  #Intensity of fringe pattern with phase shift=0
I3r= cv2.imread("I3r.png",0)  #Intensity of fringe pattern with phase shift=+2pi/3

#System setup values
l=1 #(ejemplo de valor)  #Distance between camera/projector plane and reference plane
d=1   #Distance between camera and projector
f=1   #Frequency of the projected fringe pattern

#Object
eq=np.sqrt(3)*((I1-I3)/(2*I2-I1-I3))
phase=np.arctan(eq)         #Relative phase calculation
realphase_ob=unwraping(phase)  #Absolute phase calculation

#Reference plane
eq_r=np.sqrt(3)*((I1r-I3r)/(2*I2r-I1r-I3r))
phase_r=np.arctan(eq_r)         #Relative phase calculation
realphase_r=unwraping(phase_r)  #Absolute phase calculation

#3D object reconstruction
z=3D(realphase_ob,realphase_r,l,d,f)





# Plots
fig = plt.figure(1)
plt.imsave("phasewrap2D.png",phase, cmap='gray')  #2D plot of wrapped phase


fig = plt.figure(2)
ax = plt.axes(projection='3d')
surf = ax.plot_surface(x, y, realphase,rstride=5, cstride=5,cmap='viridis', edgecolor='none')
plt.savefig("phaseunwrap.png")                         #3D plot of unwrapped phase
plt.imsave("phaseunwrap2D.png",realphase, cmap='gray') #2D plot of unwrapped phase