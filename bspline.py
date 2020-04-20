# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:15:08 2020

@author: Nick Machak, Vishesh Khanna, Dominic Fascitelli
"""

from scipy.interpolate import BSpline
import matplotlib.pyplot as plt
import numpy as np

def createTestCoefficientVector():
    return [-10,7.5,25,42.5,60,40,20,17.5,36.25,55]
    

k = 5 # order of the B spline
'''
Number of control points m+1 = n + k, where (n+1) is the number of via-points
The paper has 6 via-points in Table 2, so n = 5. So...
'''
m = 9
n = 5 #where n+1 is the number of via-points

t = [0.0027, 0.5253, 3.0691, 5.6664, 7.3138, 9.1] #time nodes for six via points
                    # This will be optimized using a NSGA 
                          
h = [t[i+1] - t[i] for i in range(len(t)-1)]

# Create knot vector
knot = [0]*(k+1) #knot0 through knot5 = 0
for i in range(k+1,n + 2*k + 1):
    if i >= n+k:
        knot.append(knot[i-1])
    else:
        knot.append(abs(h[i-k-1]))
        
knot = sorted(knot) #Knots have to be in non-decreasing order
    
h_sum = sum([abs(h) for h in h]) # sum of all the absolute value time intervals
                                 # of all the time variables

u = [knot/h_sum for knot in knot] # Normalized knot vector

spl = BSpline(knot,createTestCoefficientVector(),k) #Bspline construction

fig, ax = plt.subplots()

tt = np.linspace(0, 9, 1000)
ax.plot(tt, spl(tt), 'b-', lw=4, alpha=0.7, label='BSpline')
ax.grid(True)
ax.legend(loc='best')
plt.show()
    


