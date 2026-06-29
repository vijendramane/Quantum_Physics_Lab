"""
Transit Method Simulation
"""

import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 100, 1000)

brightness = np.ones_like(time)

brightness[450:550] = 0.98

plt.plot(time, brightness)

plt.title(
    "Exoplanet Transit Detection"
)

plt.xlabel("Time")

plt.ylabel("Star Brightness")

plt.grid()

plt.show()
