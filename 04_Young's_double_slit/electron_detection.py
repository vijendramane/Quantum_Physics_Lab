import numpy as np
import matplotlib.pyplot as plt

hits = np.random.normal(
    loc=0,
    scale=1,
    size=1000
)

plt.hist(
    hits,
    bins=50
)

plt.title(
    "Electron Detection Pattern"
)

plt.xlabel(
    "Screen Position"
)

plt.ylabel(
    "Number of Electrons"
)

plt.show()
