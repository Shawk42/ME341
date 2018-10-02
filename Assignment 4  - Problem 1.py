"""Assignment 4 Problem 2.34"""
print("Assignment 4 Problem 2.34")
"""Centrally cracked strip - Determining Max loading"""
"""Process - Find Sigma_max and use that to find force"""

import numpy as np    #Allows for matrices and other math operations
import matplotlib.pyplot as plt #Allows for plotting

"""Givens"""
Length = .02     #overall length of the strip
#Crack = .002     #length of crack
Crack = np.linspace(.0001,.01905,num=100)    #range of crack sizes up to 80% length
print(Crack)
thick = .002     #thickness of piece
K_IC = 50        #K_IC of material [MPa sqrt(m)]

"""Crack variables"""
#transfering givens into acceptable inputs for crack calculations
a = Crack/2      #half length of crack
b = Length/2     #half length of overall length
#print("a = ",a)     #troubleshooting
#print("b = ",b)     #troubleshooting

"""Sigma Calculations"""
ab = a/b                                #simplication of inputs
fab = 1+.128*ab-.288*ab**2+1.525*ab**3  #function of a/b calculation
alpha = np.sqrt(np.pi*a)                #another simplication of inputs
sigma = (K_IC/(alpha*fab))*(10**6)                #calculating sigma max

"""Force Calculations"""
Area = Length*thick        #Total area of edge
F_max = Area*sigma         #Max allowable force

#print("Max force =",F_max,"Newtons")
#print("Max force =",F_max/1000,"kN")
"""Max force is 35278 N"""

plt.plot(Crack,F_max)
plt.plot(.002,35278,'*')
plt.grid()
plt.xlabel("Crack Length (m)")
plt.ylabel("Max Mass (kg)")
plt.show()
