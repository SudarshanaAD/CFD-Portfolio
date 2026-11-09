# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 22:26:38 2026

@author: sudar
"""

# importing numpy to create array list and matplot to plot graph
import numpy as np
import matplotlib.pyplot as plt

#Chord is our length of the wing
chord = 1.0

# t is the maximum thickness as a fraction of the chord (0.12 for NACA 0012)
t = 0.12

# Mximum camber
m = 0.04

# Position of the max camber
p = 0.4

# Create 50 co-ordinates evenly spaced between 0 and chord length
x = np.linspace(0, chord, 50)

# Learn function the math formula
def calculate_thickness (x_points, thickness):
    yt = 5 * thickness * (0.2969 * np.sqrt(x_points)
                -0.1260 * x_points
                -0.3516 * x_points**2
                +0.2843 * x_points**3
                -0.1015 * x_points**4
                )
    return yt

# Calculating camber line
yc = []

for xi in x:
    if xi <= p * chord:
        formula = (m/p**2) * (2 * p * (xi/chord)-(xi/chord)**2)
    else:
        formula = (m / (1 - p)**2) * ((1 - 2 * p) + 2 * p * (xi / chord) - (xi / chord)**2)
    
    yc.append(formula) # Storing values into predefineed list
 # converting it to array list   
yc = np.array(yc)

# Calling the function
thickness_distribution = calculate_thickness(x, t)


# Upper and lower values of the airfoil
y_upper = yc + thickness_distribution
y_lower =yc - thickness_distribution


# Plots and axis
plt.plot(x, y_upper, color="blue", label="Upper Surface")
plt.plot(x, y_lower, color="red", label="Lower Surface")
plt.plot(x, yc, color="black", linestyle="--", label="Camber Line") # Added camber line visualization
plt.axis("equal")
plt.legend()
plt.show()


# Dynamic Export (Automatically creates the correct name!)
# We multiply by 100 or 10 to turn the decimals back into digits (0.04 -> 4, 0.12 -> 12)
naca_name = f"NACA{int(m*100)}{int(p*10)}{int(t*100)}"
filename = f"{naca_name}.dat"

with open(filename, "w") as file:
    # Use the dynamic name in the header too!
    file.write(f"{naca_name} Airfoil Coordinates\n")
    
    for xi, yi in zip(x[::-1], y_upper[::-1]):
        file.write(f"  {xi:.6f}   {yi:.6f}\n")
        
    for xi, yi in zip(x[1:], y_lower[1:]):
        file.write(f"  {xi:.6f}   {yi:.6f}\n")

print(f"Success! {filename} has been saved to your project folder.")


    