"""Assignment 4 - Problem 2.29"""
print("Assignment 4 - Problem 2.29")

import numpy as np

"""Givens"""
M = 1000          #Given moments
T = 2200          #Given torques
SF_accept = 3     #Acceptable safety factor
S_y = 250*(10**6) #Yield stress

"""Common Calcs"""
p = np.pi
"""Looping"""
SF = 0
D = 0.00001
while SF <= SF_accept:
    I = (p*D**4)/64
    J = (p*D**4)/32
    r = D/2
    S_zz = (M*r)/I
    S_zt = (T*r)/J
    S_E = np.sqrt((S_zz**2)+(3*S_zt**2))
    SF = S_y/S_E
    D = D+0.0001

print("Min Diameter",D*100,"cm")
print("SF",SF)