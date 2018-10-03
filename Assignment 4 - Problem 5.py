"""Assignment 4 - Problem 5"""
print("Assignment 4 - Problem 5")
import numpy as np    #Allows for matrices and other math operations
import matplotlib.pyplot as plt #Allows for plotting

"""Givens"""
P = 100*(10**3)    #Force in Newtons
thick = .01         #Thickness of plate [m]
a = np.array([.006,.03])     #Length of crack [m]
print("[6mm crack, 30mm crack]")
w = .120           #Widght of plate [m]

"""Common calcs"""
Area = thick*w        #Cross sectional area of plate
I = ((w**3)*thick)/12   #Moment of inertia
c = (.1-(w/2))         #distance between force and center axis
alpha = a/w         #Simplication of later calculations
p = np.pi           #Setting pi

"""Axial Loading"""
Sigma_a = P/Area

"""Moment Loading"""
M = c*P            #Moment
Sigma_m = (M*c)/I

"""Stress"""
Sigma_tot = Sigma_m+Sigma_a    #Superposition

"""K_I calculations"""
F_ab = 1.122-(.231*alpha)+(10.550*alpha**2)-(21.710*alpha**3)+(30.382*alpha**4)     #function of a/b calculation
K_I = Sigma_tot*np.sqrt(p*a)*F_ab
print(K_I/(10**6),"K_I","Mpa[sqrt(m)]")

"""Troubleshooting"""
#print(M,"Moment - Expect 4000")
#print(c,"distance - Expect .04")
print(Sigma_a,"Sigma a in Pa")
print(Sigma_m,"Sigma m in Pa")
#print(P,"Force in newtons")
print(Sigma_tot,"Total stress")
#print(I,"I")
#print(alpha,"alpha - Expect .025")
#print(Area,"Area of cross section - Expect .0012")