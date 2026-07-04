"""
Habitable Zone Calculator
  
Calculates the inner and outer
habitable zone boundaries.
"""

import math

def habitable_zone(luminosity):

    inner = math.sqrt(luminosity / 1.1)
    outer = math.sqrt(luminosity / 0.53)

    return inner, outer


sun_luminosity = 1.0

inner, outer = habitable_zone(
    sun_luminosity
)

print(f"Inner Boundary: {inner:.2f} AU")
print(f"Outer Boundary: {outer:.2f} AU")
