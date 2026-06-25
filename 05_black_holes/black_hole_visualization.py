import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6,6))

# Event Horizon
event_horizon = plt.Circle(
    (0,0),
    1,
    color="black",
    label="Event Horizon"
)

# Accretion Disk
disk = plt.Circle(
    (0,0),
    1.6,
    fill=False,
    linestyle="--",
    linewidth=2,
    label="Accretion Disk"
)

ax.add_artist(event_horizon)
ax.add_artist(disk)

plt.title("Simplified Black Hole Diagram")

plt.xlim(-3,3)
plt.ylim(-3,3)

plt.gca().set_aspect("equal")

plt.grid()

plt.legend()

plt.show()
