import math

G = 6.67430e-11

class CelestialBody:

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

def gravitational_force(body1, body2, distance):

    return (
        G *
        body1.mass *
        body2.mass /
        distance**2
    )

earth = CelestialBody(
    "Earth",
    5.972e24
)

moon = CelestialBody(
    "Moon",
    7.348e22
)

distance = 384400000

force = gravitational_force(
    earth,
    moon,
    distance
)

print(f"Earth-Moon Force: {force:.2e} N")

# how the actuall garvity looks
