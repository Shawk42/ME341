"""Assignment 4 - Problem 2.33"""
print("Assignment 4 - Problem 2.33")
import numpy as np    #Allows for matrices and other math operations
import matplotlib.pyplot as plt #Allows for plotting

"""Givens"""
K_IC = 77    #[Mpa sqrt(mm)]
S_y = 690    #[Mpa] in the axial
length = 2        #max crack length in mm

"""Solution"""
a = np.linspace(0,length,num=50)  #varying crack length
p = np.pi
K_I = 2*S_y*np.sqrt(a/p)

plt.plot(a,K_I)
plt.grid()
plt.show()