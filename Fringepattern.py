import numpy as np
import matplotlib.pyplot as plt

N=2048
dx=0.1
x=dx*np.arange(-N/2,N/2)
y=dx*np.arange(-N/2,N/2)

X,Y=np.meshgrid(x,y)

w=2*np.pi/1
Z0=np.cos(w*X)
Z1=np.cos(w*X +(2*np.pi/3))
Z2=np.cos(w*X -(2*np.pi/3))




plt.figure()
plt.imshow(Z0,cmap="gray")
plt.imsave("PatronI2AA.png", Z0, cmap="gray")

plt.figure()
plt.imshow(Z1,cmap="gray")
plt.imsave("PatronI3AA.png", Z1, cmap="gray")

plt.figure()
plt.imshow(Z2,cmap="gray")
plt.imsave("PatronI1AA.png", Z2, cmap="gray")

plt.show()