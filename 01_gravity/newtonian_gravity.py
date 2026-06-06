import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11

m1 = 5.972e24      # Earth mass (kg)
m2 = 1000          # Object mass (kg)

distances = np.linspace(6.4e6, 5e7, 1000)

forces = G * m1 * m2 / distances**2

plt.figure(figsize=(10, 6))
plt.plot(distances / 1000, forces)

plt.title("Newtonian Gravitational Force vs Distance")
plt.xlabel("Distance from Earth's Center (km)")
plt.ylabel("Force (N)")
plt.grid(True)

plt.show()
