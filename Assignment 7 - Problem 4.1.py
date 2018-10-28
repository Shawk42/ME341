'''Assignment 7 - Problem 4.1'''
print("Assignment 7 - Problem 1")
print(" "*50)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


"""GIVENS"""
met = .001    #Conversion factor from mm to m
b = 20*met    #Length of base                  [m]
h = 60*met    #Height of base                  [m]
theta = np.radians(25) #angle of moment in radians
M = 500  #Moment                               [N-m]

"""SOLUTION"""
#Max stress
My = np.sin(theta)*M
Mx = np.cos(theta)*M
Iy = ((b**3)*h)/2
Ix = (b*(h**3))/2
x = np.linspace(0,b/2,num=100)
y = np.linspace(0,h/2,num=100)
sigma_zz = ((-My/Iy)*x)+((Mx/Ix)*y)
sigma_zz_max = int(np.max(np.absolute(sigma_zz)))

#Location of max stress
m = (My*Ix)/(Mx*Iy)
y_loc = m*x

#Orientation
si_rad = np.arctan(m)
si = np.degrees(si_rad)


"""PRINTING"""
print("Max stress is ",sigma_zz_max,"[Pa]")
print("The neutral axis is at",si,"[degrees]")

"""Plotting"""
plt.plot(x,y_loc)
plt.title("Max stress function Graphing")
plt.xlabel("X position")
plt.xlabel("Caclulated Y position")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,sigma_zz, marker='*')
ax.set_xlabel("x")
ax.set_zlabel("Sigma_zz")
ax.set_ylabel("y")
plt.title("Stress vs. x position vs. y position")
plt.show()

axis_int = np.linspace(0,1,num = 5)
angle_int_x = axis_int/np.cos(theta)
angle_si_x = axis_int/np.cos(si_rad)
angle_int_y = axis_int/np.sin(theta)
angle_si_y = axis_int/np.sin(si_rad)
plt.plot(angle_int_x,angle_int_y)
plt.plot(angle_si_x,angle_si_y)
plt.show()