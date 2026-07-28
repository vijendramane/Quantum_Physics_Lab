"""
Galaxy with Dark Matter Halo
"""

import matplotlib.pyplot as plt

galaxy = plt.Circle((0,0),1,color="gold")

halo = plt.Circle((0,0),3,
                  fill=False,
                  linestyle="--")

fig,ax=plt.subplots(figsize=(6,6))

ax.add_patch(galaxy)

ax.add_patch(halo)

ax.set_xlim(-4,4)

ax.set_ylim(-4,4)

ax.set_aspect("equal")

plt.title("Galaxy and Dark Matter Halo")

plt.show()
