import math

# Constants
G = 6.67430e-11       # Gravitational constant
c = 299792458         # Speed of light 
M = 5.972e24          # Mass of Earth

def time_dilation(radius):
    """ 
    Calculates gravitational time dilation factor 
    around a spherical body.
    """
   
    return math.sqrt( 
        1 - (2 * G * M) / (radius * c**2)
    )

earth_surface = 6_371_000       # meters
gps_orbit = 26_571_000          # meters

surface_time = time_dilation(earth_surface)
gps_time = time_dilation(gps_orbit)

print("Earth Surface Time Factor:", surface_time)
print("GPS Orbit Time Factor:", gps_time)

difference = gps_time - surface_time

print("\nDifference:", difference)

# Time dilation via curvature of space in space

