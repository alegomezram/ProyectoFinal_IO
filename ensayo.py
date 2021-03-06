import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt




phase=[1.55815429,  1.41461946,  1.26041304,
  1.09314882,  0.92410509,  0.75897582,  0.62164677,  0.48178616,  0.36300343,
  0.26197903,  0.15990703,  0.07576133, -0.01374557, -0.10396422, -0.19620289,
 -0.28554541, -0.39554182, -0.52359877, -0.65387633, -0.81091669, -0.97557849,
 -1.15140495, -1.31491907, -1.46775653,  1.54569941,  1.4264317,   1.31961544,
  1.22120306,  1.12992562,  1.05176759,  0.95772925,  0.87226421,  0.77362179,
  0.66290422,  0.55266575,  0.41373039,  0.2592971,   0.09170932, -0.07891323,
 -0.25091089, -0.40353863, -0.54159579, -0.65981868, -0.76392486, -0.86614005,
 -0.95772925, -1.04035161, -1.12948989, -1.22074281, -1.31700043, -1.41290038,
 -1.53733924]

print("1",phase)
plt.figure(1)
plt.plot(phase)
plt.savefig("1.png")

phase=np.array(phase)
phase=phase*2*np.pi
plt.figure(2)
plt.plot(phase)
plt.savefig("2.png")
print("2",phase)

p=np.unwrap(phase)
print("3",p)
plt.figure(3)
plt.plot(p)
plt.savefig("3.png")

# l1 =[1, 2, 3, 4, 5]
# print("Result 1: ", np.unwrap(l1))
 
# l2 =[0, 0.78, 5.49, 6.28]
# print("Result 2: ", np.unwrap(l2))