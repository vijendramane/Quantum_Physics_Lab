"""
Gravitational Time Dilation
"""

import math

G = 6.67430e-11
C = 299792458 

earth_mass = 5.972e24
earth_radius = 6_371_000


def time_dilation(mass, radius):

    return math.sqrt(
        1 -
        (2 * G * mass) /
        (radius * C ** 2)
    )


factor = time_dilation(
    earth_mass,
    earth_radius
)

print("Time Dilation Factor")
print(factor)
