"""
Galaxy Rotation Curve
"""

import numpy as np
import matplotlib.pyplot as plt

distance = np.linspace(1, 30, 200)

# Newtonian prediction
velocity_newton = 220 / np.sqrt(distance)

# Observed rotation curve
velocity_dark = np.full_like(distance, 220)

plt.figure(figsize=(8,5))

plt.plot(distance, velocity_newton,
         label="Without Dark Matter")

plt.plot(distance, velocity_dark,
         label="Observed")

plt.xlabel("Distance from Galactic Center (kpc)")
plt.ylabel("Orbital Velocity (km/s)")
plt.title("Galaxy Rotation Curve")
plt.grid(True)
plt.legend()

plt.show()
