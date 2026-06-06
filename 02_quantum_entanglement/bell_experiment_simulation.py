import random

trials = 1000

same_results = 0 

for _ in range(trials):

    particle_a = random.choice([0, 1])
  
    particle_b = particle_a

    if particle_a == particle_b:
        same_results += 1

print("Trials:", trials)

print(
    "Correlation:",
    same_results / trials
)
