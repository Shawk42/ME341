'''ASSIGNMENT 7 - PROBLEM 4.8'''
print("Assignment 7 - Problem 4.8")

import numpy as np
import matplotlib.pyplot as plt

"""GIVENS"""
mfour = 1*(10**-12)    #Conversion from mm^4 to m^4
I_x = 560000*mfour    #Ix               [m^4]
I_y = 290000*mfour    #Iy               [m^4]
I_xy = 300000*mfour   #Ixy              [m^4]
L = 2                 #Length of beam   [m]
w = 1000              #Distributed load [N/m]

n = 1000               #Mesh size of calculation

"""MAX MOMENT ALONG BEAM"""
#Finding reaction forces
F = w*L                       #Point load of distributed load
x_beam = np.linspace(0,L,n)   #Linearly space array of lengths
M = ((w*x_beam)/2)*(L-x_beam) #Bending Moment
M_max = np.amax(M)            #Extracting the max moment
M_ind = list(M).index(M_max)  #Extracting the array position of the maximum moment
M_pos = x_beam.item(M_ind)         #Extracting the physical position of the max moment

"""MAX STRESS CALCULATIONS"""
x = np.linspace(0,(35*.001),n)          #X position in cross section
y = np.linspace(0,(30*.001),n)          #Y position in cross section
M_x = M_pos                      #Changing variable name for equation

sigma_zz = (((M_x*I_xy)/(I_xy**2))*x)-(((M_x*I_y)/I_xy**2)*y)  #Calculating stress in cross section

sigma_max = np.amax(sigma_zz)                    #Max Stress value
sig_max_index = list(sigma_zz).index(sigma_max)  #At what point in the array is the stress maximized
x_pos = x.item(sig_max_index)
y_pos = y.item(sig_max_index)

"""PRINTING"""
print(""*50)
print("RESULTS")
print("-"*50)
print("The max moment is",M_max,"[N-m]")
print("The max moment occurs at",M_pos,"[m]")
print("The max bending stress is",sigma_max,"[Pa]")
print("The max bending stress occurs at (x,y)",x_pos,",",y_pos,"[m]")

"""PLOTTING"""
plt.plot(x_beam,M)
plt.plot(M_pos,M_max,'*')
plt.title("Bending Moment Diagram")
plt.xlabel("Position [meters]")
plt.ylabel("Bending Moment [Nm]")
plt.grid()
plt.show()
