"""
Exoplanet Classifier
"""

def classify(radius):

    if radius < 1.25:
        return "Earth-like"

    elif radius < 2:
        return "Super-Earth"

    elif radius < 6:
        return "Mini-Neptune"

    else:
        return "Gas Giant"


planet_radius = 1.8

print(
    classify(planet_radius)
)
