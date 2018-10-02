"""Assigment 4 - Problem 2.28"""
print("Assignment 4 - Problem 2.28")
import numpy as np

"""Givens and common calcs"""
T = 5000       #Initial torque on shaft
J = np.pi/32   #Polar molar of area

"""Von Mises"""
Torque = T/J
Sig_E = np.sqrt(3*Torque**2)
Moment = Sig_E                #Max moment

Check = np.sqrt(Moment**2)
if Check+Moment:
    print("Correct")
    print("Max moment Von Mises = ",Moment)
else:
    print("Moment does not match up")

"""Tresca"""


