"""
Galaxy Mass Estimator
""" 

G = 6.67430e-11
 
velocity = 220000      # m/s 

radius = 50000 * 9.461e15 

mass = velocity**2 * radius / G

solar_mass = 1.989e30

print("Estimated Galaxy Mass")

print(f"{mass/solar_mass:.2e} Solar Masses")
