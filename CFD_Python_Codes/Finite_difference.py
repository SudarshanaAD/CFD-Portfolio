# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#getting the numpy module
import numpy as np

#Defining polynomial
poly_p = np.array([-4,7,-3,9])

#Polynomial derivative
poly_der = np.polyder(poly_p)
#confirmation of correct derivative polynomial
print('Derivative polynomial = ', poly_der)

#Analytical results at x=0
poly_der_val = np.polyval(poly_der,0.0)
#confirmation of derivative @ x=0
print('theoritical derivative =',poly_der_val)

#Numerical calculation using FDM (forward)
x_0 = 0.0
h =np.float64(0.25)
forward_difference = (np.polyval(poly_p,x_0+h)-np.polyval(poly_p,x_0))/h
print('Forward difference = ', forward_difference)

#Numerical calculation using BDM (Backward)
backward_difference = (np.polyval(poly_p,x_0)-np.polyval(poly_p,x_0-h))/h
print('Backward difference = ', backward_difference)

#Numerical calculation using CDM (Central)
central_difference = (np.polyval(poly_p,x_0+h)-np.polyval(poly_p,x_0-h))/h
print('Central difference = ', central_difference)