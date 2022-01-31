import numpy as np
import matplotlib.pyplot as plt

N=2048
dx=0.1
x=dx*np.arange(-N/2,N/2)
y=dx*np.arange(-N/2,N/2)

X,Y=np.meshgrid(x,y)

w=2*np.pi/20
Z0=np.cos(w*X)
Z1=np.cos(w*X +(2*np.pi/3))
Z2=np.cos(w*X -(2*np.pi/3))



def minmax(v):
    if v > 255:
        v = 255
    if v < 0:
        v = 0
    return v


def dithering_gray(inMat, samplingF):
    #https://en.wikipedia.org/wiki/Floyd–Steinberg_dithering
    #https://www.youtube.com/watch?v=0L2n8Tg2FwI&t=0s&list=WL&index=151
    #input is supposed as color
    # grab the image dimensions
    h = inMat.shape[0]
    w = inMat.shape[1]
    
    # loop over the image
    for y in range(0, h-1):
        for x in range(1, w-1):
            # threshold the pixel
            old_p = inMat[y, x]
            new_p = np.round(samplingF * old_p/255.0) * (255/samplingF)
            inMat[y, x] = new_p
            
            quant_error_p = old_p - new_p
            


            # inMat[y, x+1] = minmax(inMat[y, x+1] + quant_error_p * 7 / 16.0)
            # inMat[y+1, x-1] = minmax(inMat[y+1, x-1] + quant_error_p * 3 / 16.0)
            # inMat[y+1, x] = minmax(inMat[y+1, x] + quant_error_p * 5 / 16.0)
            # inMat[y+1, x+1] = minmax(inMat[y+1, x+1] + quant_error_p * 1 / 16.0)
            
            inMat[y, x+1] = minmax(inMat[y, x+1] + quant_error_p * 7 / 16.0)
            inMat[y+1, x-1] = minmax(inMat[y+1, x-1] + quant_error_p * 3 / 16.0)
            inMat[y+1, x] = minmax(inMat[y+1, x] + quant_error_p * 5 / 16.0)
            inMat[y+1, x+1] = minmax(inMat[y+1, x+1] + quant_error_p * 1 / 16.0)


            #   quant_error  := oldpixel - newpixel
            #   pixel[x + 1][y    ] := pixel[x + 1][y    ] + quant_error * 7 / 16
            #   pixel[x - 1][y + 1] := pixel[x - 1][y + 1] + quant_error * 3 / 16
            #   pixel[x    ][y + 1] := pixel[x    ][y + 1] + quant_error * 5 / 16
            #   pixel[x + 1][y + 1] := pixel[x + 1][y + 1] + quant_error * 1 / 16


    # return the thresholded image
    return inMat

plt.figure()
plt.imshow(Z0,cmap="gray")
plt.imsave("PatronI2.png", Z0, cmap="gray")

plt.figure()
plt.imshow(Z1,cmap="gray")
plt.imsave("PatronI3.png", Z1, cmap="gray")

plt.figure()
plt.imshow(Z2,cmap="gray")
plt.imsave("PatronI1.png", Z2, cmap="gray")

plt.show()