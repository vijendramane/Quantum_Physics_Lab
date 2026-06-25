"""
Escape Velocity Calculator
"""

import math
 
G = 6.67430e-11


def escape_velocity(mass, radius):
    return math.sqrt((2 * G * mass) / radius)


earth_mass = 5.972e24
earth_radius = 6_371_000

velocity = escape_velocity(
    earth_mass,
    earth_radius
)

print(
    f"Escape Velocity: {velocity/1000:.2f} km/s"
)
