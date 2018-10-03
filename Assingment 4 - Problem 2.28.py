"""Assigment 4 - Problem 2.28"""
print("Assignment 4 - Problem 2.28")
import numpy as np

"""Givens and common calcs"""
T = 5000       #Initial torque on shaft
J = np.pi/32   #Polar molar of area
I = np.pi/64

"""Von Mises"""
Torque = T/J
Sig_E = np.sqrt(3*Torque**2)
Moment = Sig_E*I                #Max moment

Check = np.sqrt(Moment**2)
if Check+Moment:
    print("Correct")
    print("Max moment Von Mises = ",Moment/1000,"kNm")
else:
    print("Moment does not match up")

"""Tresca"""
Moment_tresca = (T/J)*I
print("Max moment Tresca = ",Moment_tresca/1000,"kNm")

