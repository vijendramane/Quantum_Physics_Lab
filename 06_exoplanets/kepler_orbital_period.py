"""
Kepler's Third Law
"""

import math

def orbital_period(distance_au):

    return math.sqrt(distance_au ** 3)


earth_distance = 1.0

period = orbital_period(
    earth_distance
)

print(
    f"Orbital Period: {period:.2f} years"
)
