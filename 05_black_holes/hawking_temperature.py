"""
Hawking Temperature
"""

import math

G = 6.67430e-11
HBAR = 1.054571817e-34
C = 299792458
K = 1.380649e-23


def hawking_temperature(mass):

    return (
        HBAR * C ** 3
    ) / (
        8 *
        math.pi *
        G *
        mass *
        K
    )


solar_mass = 1.989e30

temp = hawking_temperature(solar_mass)

print(f"Hawking Temperature: {temp:.20f} Kelvin")
