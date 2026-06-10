import math

# Example values
barrier_width = 1e-9  # meters
kappa = 1e10

# Tunneling probability
T = math.exp(-2 * kappa * barrier_width)

print("Barrier Width:", barrier_width, "m")
print("Tunneling Probability:", T)
