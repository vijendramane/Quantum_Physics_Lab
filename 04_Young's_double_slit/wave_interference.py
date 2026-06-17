import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 1000)

wave1 = np.sin(x)
wave2 = np.sin(x + np.pi/2)

interference = wave1 + wave2

plt.figure(figsize=(10, 5))
plt.plot(x, wave1, label="Wave 1")
plt.plot(x, wave2, label="Wave 2")
plt.plot(x, interference, label="Interference")

plt.title("Wave Interference")
plt.xlabel("Position")
plt.ylabel("Amplitude")

plt.legend()
plt.grid(True)

plt.show()
