import numpy as np

# |00>
state_00 = np.array([1, 0, 0, 0])

# Bell State
bell_state = (1 / np.sqrt(2)) * np.array([1, 0, 0, 1])

print("Bell State:")
print(bell_state)

probabilities = np.abs(bell_state) ** 2

print("\nProbabilities:")
print("|00> =", probabilities[0])
print("|01> =", probabilities[1])
print("|10> =", probabilities[2])
print("|11> =", probabilities[3])
