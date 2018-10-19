"""The intention of this code is to explore the relationships of sudden vs slow loading"""
import numpy as np
import matplotlib.pyplot as plt

"""Common paramters"""
"""Using the spring  https://www.mcmaster.com/9657k294"""
L = 1      #Length of spring
K = 14.95  #Spring rate in lbs/in
m_max = 6  #Max load in lbs
L_min = 0.6 #Length at max loading

"""User defined inputs"""
F = np.linspace(0,6, num=10000)      #Force of the mass [aka weight]
h = (F/3)+((1/F)+.25)

"""Slow loading [Filling a bucket on water on the spring]"""
u_1 = F/K
h_1 = L-u_1  #height of mass above ground

"""Sudden Loading"""
u_2 = (F/K)+np.sqrt(((F/K)**2)+((2*F*h)/K))
h_2 = L-u_2 #height of mass above ground

"""Eqiilrium height-Min height"""
delta = h_1-h_2

"""Printing"""
#print(h_1, "h_1", u_1, "u_1")
#print(h_2, "h_2", u_2, "u_2")

"""Plotting"""
plt.plot(F,h_1)
plt.plot(F,h_2)
plt.plot(F,delta)
plt.xlabel("Force")
plt.ylabel("Mass height above ground")
plt.grid()
plt.show()
