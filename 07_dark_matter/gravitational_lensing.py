"""
Simple Gravitational Lensing Visualization
"""
 
import numpy as np
import matplotlib.pyplot as plt 

theta = np.linspace(0,2*np.pi,300)

r = 1 + 0.15*np.sin(2*theta)

x = r*np.cos(theta)
y = r*np.sin(theta)

plt.figure(figsize=(6,6))

plt.plot(np.cos(theta),np.sin(theta),
         '--',label="Original")

plt.plot(x,y,label="Lensed")

plt.axis("equal")

plt.title("Gravitational Lensing")

plt.legend()

plt.show()
