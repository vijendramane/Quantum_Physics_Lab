""" 
Chapter 05 - Black Holes

Schwarzschild Radius Calculator
"""

import math

G = 6.67430e-11
C = 299792458


def schwarzschild_radius(mass):
    """
    Calculate Schwarzschild Radius.

    Parameters:
        mass (kg)

    Returns:
        radius (meters)
    """

    return (2 * G * mass) / (C ** 2)


earth_mass = 5.972e24
sun_mass = 1.989e30

print("Earth")
print(f"Radius: {schwarzschild_radius(earth_mass):.6f} meters")

print()

print("Sun")
print(f"Radius: {schwarzschild_radius(sun_mass):.2f} meters")
