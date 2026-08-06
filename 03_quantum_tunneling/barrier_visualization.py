import numpy as np
import matplotlib.pyplot as plt
 
x = np.linspace(0, 10, 1000)

barrier = np.where((x >= 4) & (x <= 6), 8, 0)

particle_energy = np.ones_like(x) * 5

plt.figure(figsize=(10, 5))
plt.plot(x, barrier, label="Barrier Height")
plt.plot(x, particle_energy, label="Particle Energy") 

plt.title("Quantum Tunneling Concept")
plt.xlabel("Position")
plt.ylabel("Energy")

plt.legend()
plt.grid(True)

plt.show()
