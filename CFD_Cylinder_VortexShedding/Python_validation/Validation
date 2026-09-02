# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 23:02:27 2026

@author: sudar
"""
# Flow over a cylinder simulation (simplified)
# Using Python + NumPy to set up parameters

import numpy as np   # Import numerical library for arrays and math
import matplotlib.pyplot as plt  # For plotting results

# -----------------------------
# 1. Define physical parameters
# -----------------------------
D = 0.1        # Cylinder diameter [m]
U = 0.0147     # Inlet velocity [m/s]
rho = 1.225    # Air density [kg/m^3]
mu = 1.8e-5    # Dynamic viscosity [Pa·s]

# -----------------------------
# 2. Calculate Reynolds number
# -----------------------------
Re = (rho * U * D) / mu   # Formula: Re = (ρ U D) / μ
print("Reynolds number =", Re)

# -----------------------------
# 3. Time-stepping parameters
# -----------------------------
dt = 0.01      # Time step size [s]
t_end = 2.0    # Total simulation time [s]
time = np.arange(0, t_end, dt)  # Create array of time steps

# -----------------------------
# 4. Placeholder for lift/drag
# -----------------------------
Cl = np.sin(2 * np.pi * 0.16 * time)   # Approximate oscillation (Strouhal ~ 0.16)
Cd = 1.0 + 0.2 * np.cos(2 * np.pi * 0.16 * time)  # Drag oscillation

# -----------------------------
# 5. Plot results
# -----------------------------
plt.figure(figsize=(8,4))
plt.plot(time, Cl, label="Lift Coefficient (Cl)")
plt.plot(time, Cd, label="Drag Coefficient (Cd)")
plt.xlabel("Time [s]")
plt.ylabel("Coefficient")
plt.title("Vortex Shedding over Cylinder (Re=100)")
plt.legend()
plt.grid(True)
plt.show()
