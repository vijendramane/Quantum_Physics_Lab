import random

def measure_entangled_pair():
    
    result = random.choice([0, 1])

    particle_a = result
    particle_b = result

    return particle_a, particle_b

for i in range(10):
    
    a, b = measure_entangled_pair()

    print(
        f"Measurement {i+1}: "
        f"Particle A = {a}, "
        f"Particle B = {b}"
    )
