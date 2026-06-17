import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 2000)

wavelength = 1
slit_distance = 2

intensity = (
    np.cos(
        np.pi *
        slit_distance *
        x /
        wavelength
    )
) ** 2

plt.figure(figsize=(10, 5))

plt.plot(
    x,
    intensity
)

plt.title(
    "Double Slit Interference Pattern"
)

plt.xlabel(
    "Screen Position"
)

plt.ylabel(
    "Intensity"
)

plt.grid(True)

plt.show()
