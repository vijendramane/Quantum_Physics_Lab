"""
Star Light Curve
"""

import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 50, 500)

brightness = ( 
    1
    - 0.02 *
    np.exp(
        -((time - 25) ** 2) / 4
    )
)

plt.plot(
    time,
    brightness
)

plt.title(
    "Star Light Curve"
)

plt.xlabel("Time")

plt.ylabel("Brightness")

plt.grid()

plt.show()
