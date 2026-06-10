import random

particles = 1000
tunneling_probability = 0.15

tunneled = 0
 
for _ in range(particles):

    if random.random() < tunneling_probability:
        tunneled += 1

blocked = particles - tunneled

print("Total Particles:", particles)
print("Tunneled:", tunneled)
print("Blocked:", blocked)

print(
    "Observed Probability:",
    tunneled / particles
)
