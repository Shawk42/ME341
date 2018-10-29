'''Assignment 7 - Problem 4.5'''
print("Assignment 7 - Problem 4.5")

import numpy as np
import matplotlib.pyplot as plt

"""GIVENS"""
Nmm = 1000
I_x = 15*(10**6)      #MOI for x direction    [mm^4]
I_y = 0.637*(10**6)   #MOI for y direction    [mm^4]
M_x = 2200*Nmm        #Moment in x direction  [N-mm]
M_y = -350*Nmm        #Moment in y direction  [N-mm]
y_max = 203/2         #Centroid to top        [mm]
x_max = 59.5-15.6     #Centroid to right flange [mm]

"""INTERMEDIATE STEPS"""
n = 100                  #"Mesh size"
x = np.linspace(-15.6,x_max,n)
y = np.linspace(0,y_max,n)
zero = np.zeros(n)

"""Stress caclulations"""
sigma_zz = ((-M_y/I_y)*x)+((M_x/I_x)*y)


"""Graphing"""
plt.plot(x,sigma_zz)
plt.plot(y,sigma_zz)
plt.plot(x,zero)
plt.plot(zero,y)
plt.show()