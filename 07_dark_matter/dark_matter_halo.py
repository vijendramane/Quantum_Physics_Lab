"""
Dark Matter Halo Density
"""

import numpy as np
import matplotlib.pyplot as plt

radius = np.linspace(0.1,50,300)

density = 1/(1+radius**2)

plt.figure(figsize=(8,5))

plt.plot(radius,density)

plt.title("Dark Matter Halo Density")

plt.xlabel("Radius")

plt.ylabel("Relative Density")

plt.grid(True)

plt.show()
