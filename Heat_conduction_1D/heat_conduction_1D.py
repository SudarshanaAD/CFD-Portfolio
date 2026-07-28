# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 18:19:14 2026

@author: sudar
"""

# importing numpy
import numpy as np

# getting the matplotlib
import matplotlib.pyplot as plt

# initializing variables

# Number of grid points
N=11

# Domain size
L=1

# Corresonding grid spacing
h = np.float64(L/(N-1))

# iteration number
iteration = 0

# initializing temperature field
T = np.zeros(N)
T[N-1] = 1. 

# initializing iterated temperature 
T_new = np.zeros(N)
T_new[N-1] = 1. 

# error related variable
epsilon = 1.E-8
numerical_error = 1

#checking the error tolerance
while numerical_error > epsilon:
    #computing for all iteration values
    for i in range (1,N-1):
        T_new[i] = 0.5*( T[i-1] + T[i+1])
        
    # resulting the numerical error and recalculate 
    numerical_error = 0
    for i in range (1,N-1):
        numerical_error = numerical_error + abs (T[i]-T_new[i])
        
    # iteration advancement and reassignment
    iteration = iteration + 1
    T = T_new.copy()
    
# plotting the results

# defining the position vectors from indices
x_dom = np.arange (N) * h

# plotting the variation with customization
plt.plot (x_dom, T, 'gx-', linewidth=2, markersize=8)

# display the grid lines
plt.grid (True, color = 'k')

# labeling and providing a title to the plot 
plt.xlabel("position", size=20)
plt.ylabel("temperature", size=20)
plt.title("T(x)")

# Showing the plot on the screen
plt.show()
