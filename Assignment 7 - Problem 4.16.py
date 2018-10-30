'''ASSIGNMENT 7 - PROBLEM 4.16'''
print("Assignment 7 - Problem 4.16")

import numpy as np
import matplotlib.pyplot as plt

"GIVENS"
#[Section 1 , Section 2] {around O prim}
x_length = np.array([100,20])    #Length of each cross section in the x direction [mm]
y_length = np.array([20,180])    #Length of each cross section in the xi direction [mm]
cen_x = np.array([50,10])        #Local centroid dist from O' [mm]
cen_y = np.array([10,120])       #Local centroid dist from O' [mm]

"CENTROID CALCULATIONS"
area_local = np.multiply(x_length,y_length)   #Finding areas of each cross section
area_sum = np.sum(area_local)                 #Finding the total cross sectional area
cen_x_sum = np.sum(cen_x)                     #Summing the local centroids
cen_y_sum = np.sum(cen_y)                     #Summing the local centroids
alpha_x = area_sum*cen_x_sum
alpha_y = area_sum*cen_y_sum
centroid_x = alpha_x/area_sum        #Finding the centroid in the x direction
centroid_y = alpha_y/area_sum        #Finding the centroid in the y direction

"""PRINTING"""
print("X location centroid",centroid_x)
print("Y location centroid",centroid_y)

print("Sum of local x centroids",cen_x_sum)
print("Sum of local y centroids",cen_y_sum)