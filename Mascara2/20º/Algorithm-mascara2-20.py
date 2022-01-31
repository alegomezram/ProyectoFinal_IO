import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits import mplot3d
import numpy as np
import time
import cv2
from PIL import Image
from skimage import data, img_as_float, color, exposure
from skimage.restoration import unwrap_phase

#Functions

def unwraping(phase):

	#phase unwrapping

	#absolutephase=(np.unwrap(np.unwrap(phase,axis=0), axis=-1))
	absolutephase = unwrap_phase(phase) #skimage function


	return absolutephase


def reconst(phaseobj,phaseref,l,d,f):

	#Depth information acquisition

	deltaph=phaseobj-phaseref   #phase difference

	z=(l/d)*(deltaph)  #option1

#	z=(l*deltaph)/(deltaph+(2*np.pi*d*f))  #option2

#	z=10+1*(deltaph)   #option3

	return z


# #Import pictures of object
# I1= cv2.imread("I1.png",-1)  #Intensity of fringe pattern with phase shift=-2pi/3
# I2= cv2.imread("I2.png",-1)  #Intensity of fringe pattern with phase shift=0
# I3= cv2.imread("I3.png",-1)  #Intensity of fringe pattern with phase shift=+2pi/3

# #Import pictures of reference plane
# I1r= cv2.imread("I1r.png",-1)  #Intensity of fringe pattern with phase shift=-2pi/3
# I2r= cv2.imread("I2r.png",-1)  #Intensity of fringe pattern with phase shift=0
# I3r= cv2.imread("I3r.png",-1)  #Intensity of fringe pattern with phase shift=+2pi/3

#Import pictures of object
I1= Image.open("I1f.tif")  #Intensity of fringe pattern with phase shift=-2pi/3
I2= Image.open("I2f.tif")  #Intensity of fringe pattern with phase shift=0
I3= Image.open("I3f.tif")  #Intensity of fringe pattern with phase shift=+2pi/3

#Import pictures of reference plane
I1r= Image.open("I1rf.tif")  #Intensity of fringe pattern with phase shift=-2pi/3
I2r= Image.open("I2rf.tif")  #Intensity of fringe pattern with phase shift=0
I3r= Image.open("I3rf.tif")  #Intensity of fringe pattern with phase shift=+2pi/3

#Convert to arrays
I1 = np.array(I1)
#print("I1",I1)
I2 = np.array(I2)
#print("I2",I2)
I3 = np.array(I3)
#print("I3",I3)

I1r = np.array(I1r)
I2r = np.array(I2r)
I3r = np.array(I3r)

np.set_printoptions(threshold=np.inf)

#System setup values and real coordinates
#All units in um
l=400000  #(40cm)  #Distance between camera/projector plane and reference plane
d=130000   #(13cm)Distance between camera and projector
f=10000   #Frequency of the projected fringe

M=1024 #Number of pixels along x axis
N=1024 #Number of pixels along y axis
dx=5.86 #size of pixels (35um)
dy=5.86
u=M/2*dx  #image size (width of camera 36mm)
v=N/2*dy
xx=np.linspace(-u,u,num=M)
yy=np.linspace(-v,v,num=N)
x,y=np.meshgrid(xx,yy)


#Object
#eq=np.zeros((1024,1024))
#mat1=I1-I3
#mat2=2*I2-I1-I3
#lp=np.where(mat2!= 0)         #to avoid divisions by zero
#eq[lp]=np.sqrt(3)*(mat1[lp]/mat2[lp])
#eq=np.sqrt(3)*((I1-I3)/(2*I2-I1-I3))
phase=np.arctan2(np.sqrt(3)*(I1-I3), 2*I2-I1-I3)            #Relative phase calculation
realphase_ob=unwraping(phase)  #Absolute phase calculation


#Reference plane
# eq_r=np.zeros((1024,1024))
# mat1r=I1r-I3r
# mat2r=2*I2r-I1r-I3r
# lr=np.where(mat2r!= 0)          #to avoid divisions by zero
# eq_r[lr]=np.sqrt(3)*(mat1r[lr]/mat2r[lr])
#eq_r=np.sqrt(3)*((I1r-I3r)/(2*I2r-I1r-I3r))
phase_r=np.arctan2(np.sqrt(3)*(I1r-I3r), 2*I2r-I1r-I3r)         #Relative phase calculation
#slicee=phase_r[512,:]
#print(phase_r[512,:])
#plt.plot(xx,slicee)
#plt.savefig("slicee.png")
realphase_r=unwraping(phase_r)  #Absolute phase calculation
#plt.plot(xx,realphase_r)              
#plt.savefig("unwrappedslicee.png")

#3D object reconstruction
z=reconst(realphase_ob,realphase_r,l,d,f)

#minimum=np.min(z)
#l=np.where(z>-20.) 
#z[l]=-32.




# Plots
# plt.figure(1)
# #ax = plt.axes(projection='3d')
# #surf = ax.plot_surface(x, y, z,rstride=5, cstride=5,cmap='viridis', edgecolor='none')
# plt.imshow(I1, cmap='gray')
# plt.figure(4)
# plt.imshow(phase, cmap='gray')

# plt.figure(2)
# plt.imshow(realphase_r, cmap='gray')

# plt.figure(3)
# plt.imshow(z, cmap='gray')

#Object
fig = plt.figure(1)
plt.imsave("1phasewrap_obj2D.png",phase,cmap='gray')  #2D plot of wrapped phase

#Reference plane
fig = plt.figure(2)
plt.imsave("2phasewrap_ref2D.png",phase_r, cmap='gray')  #2D plot of wrapped phase

#Object
fig = plt.figure(3)
ax = plt.axes(projection='3d')
surf = ax.plot_surface(x, y, realphase_ob,rstride=5, cstride=5,cmap='viridis', edgecolor='none')
plt.savefig("phaseunwrap_obj.png")                         #3D plot of unwrapped phase
plt.imsave("3phaseunwrap_obj2D.png",realphase_ob, cmap='gray') #2D plot of unwrapped phase

#Reference plane
fig = plt.figure(4)
ax = plt.axes(projection='3d')
surf = ax.plot_surface(x, y, realphase_r,rstride=5, cstride=5,cmap='viridis', edgecolor='none')
plt.savefig("phaseunwrap_ref.png")                         #3D plot of unwrapped phase
plt.imsave("4phaseunwrap_ref2D.png",realphase_r, cmap='gray') #2D plot of unwrapped phase



#Reconstruction
fig = plt.figure(5)
ax = plt.axes(projection='3d')
surf = ax.plot_surface(x, y, z,rstride=5, cstride=5,cmap='viridis', edgecolor='none')
#ax.view_init(40, 10)
plt.savefig("reconstruction3D2.png")                         #3D plot of unwrapped phase
plt.imsave("5reconstruction2D2.png",z, cmap='gray') #2D plot of unwrapped phase


