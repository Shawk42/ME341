'''Assignment 7 - Problem 4.5'''
print("Assignment 7 - Problem 4.5")
print(" "*50)

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

"MAX VALUE EXTRACTION"
sigma_max = np.amax(sigma_zz)                    #Max Stress value
sig_max_index = list(sigma_zz).index(sigma_max)  #At what point in the array is the stress maximized

x_pos = x.item(sig_max_index)
y_pos = y.item(sig_max_index)

"""ANSWER VALIDATION"""
if x_pos > 59.5-15.6:
    print("X position is INVALID",x_pos)
else:
    print("X position is valid")
if y_pos > 203/2:
    print("Y position is INVALID",x_pos)
else:
    print("Y position is valid")


"""PRINTING"""
print(""*50)
print("RESULTS")
print("-"*50)
print("The max stress is",sigma_max,"[MPa]")
print("The max stress occurs at (x,y)",x_pos,",",y_pos,"[mm]")