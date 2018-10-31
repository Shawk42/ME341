'''ASSIGNMENT 7 - PROBLEM 4.16'''
print("Assignment 7 - Problem 4.16")

import numpy as np
import matplotlib.pyplot as plt

"""GIVENS"""
#[Section 1 , Section 2] {around O prim}
x_length = np.array([100,20])    #Length of each cross section in the x direction [mm]
y_length = np.array([20,180])    #Length of each cross section in the xi direction [mm]
cen_x = np.array([50,10])        #Local centroid dist from O' [mm]
cen_y = np.array([10,120])       #Local centroid dist from O' [mm]

"""CENTROID CALCULATIONS"""
area_local = np.multiply(x_length,y_length)   #Finding areas of each cross section
area_sum = np.sum(area_local)                 #Finding the total cross sectional area
cen_x_sum = np.sum(cen_x)                     #Summing the local centroids
cen_y_sum = np.sum(cen_y)                     #Summing the local centroids
alpha_x = area_sum*cen_x_sum
alpha_y = area_sum*cen_y_sum
centroid_x = alpha_x/area_sum        #Finding the centroid in the x direction
centroid_y = alpha_y/area_sum        #Finding the centroid in the y direction

"""LOCAL MOMENT OF INERTIA CALCULATIONS"""
b_1 = x_length.item(0)           #Pulling the base length out of array
h_1 = y_length.item(0)          #Pulling the height out of the array
b_2 = x_length.item(1)           #Pulling  the base length out of array
h_2 = y_length.item(1)          #Pulling the height out of the array
Ix_local = np.array([(b_1*(h_1**3))/12,(b_2*(h_2**3))/12])       #Calculating local MOI in X
Iy_local = np.array([(h_1*(b_1**3))/12,(h_2*(b_2**3))/12])       #Calculating local MOI in Y

"""TOTAL MOMENT OF INTERIA CALCULATIONS"""
dx_1 = centroid_x-cen_x.item(0)            #Distance from local centroid to global centroid
dy_1 = centroid_y-cen_y.item(0)
dx_2 = centroid_x-cen_x.item(1)
dy_2 = centroid_y-cen_y.item(1)
area_1 = area_local.item(0)
area_2 = area_local.item(1)
Ix_1 = Ix_local.item(0)+((dx_1**2)*area_1)        #MOI of each cross section
Ix_2 = Ix_local.item(1)+((dx_2**2)*area_2)
Iy_1 = Iy_local.item(0)+((dy_1**2)*area_1)
Iy_2 = Iy_local.item(1)+((dy_2**2)*area_2)

I_x = Ix_1+Ix_2        #Total MOI in the x direction
I_y = Iy_1+Iy_2        #Total MOI in the y direction

"""PRINTING"""
print("X location centroid",centroid_x)
print("Y location centroid",centroid_y)
print("MOI_x",int(I_x),"[mm^4]")
print("MOI_y",int(I_y),"[mm^4]")