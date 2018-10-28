'''
The intention of this script is to calculate the shear and bending moment of a simply loaded beam.
The first case is a beam with two pin supports and a single downward force at the center
'''

import numpy as np
import matplotlib.pyplot as plt

"""INPUTS"""
x = 1       #Length of beam
F = -3       #Force applied
x_f = .5    #Where the Force is applied
num = 10   #Mesh size of calculation
sections = 2   #How many different bending moments are expected

"""Intermediate Caclulations"""
zeta = int(num/sections)
orient_1 = np.full((1,zeta),-1)
orient_2 = np.full((1,zeta),1)
orient = np.append(orient_1,orient_2)
dist = np.linspace(0,x,num)

moment_raw = F*np.multiply(dist,orient)

moment = np.abs(moment_raw)

"Plotting"
plt.plot(dist,moment)
plt.show()

