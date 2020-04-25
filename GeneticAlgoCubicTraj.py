# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 01:33:31 2020

@author: Nick Machak, Vishesh Khanna, Dominic Fascitelli
"""

from platypus import NSGAII, Problem, Real
import numpy as np
import matplotlib.pyplot as plt

def cubicTraj(values):
    theta0 = 15
    thetaf = 75
    t0 = 0
    tf = values[0]
    
    a3 = (-2/tf**3)*(thetaf - theta0)
    a2 = (3/tf**2)*(thetaf - theta0)
    a1 = 0
    a0 = theta0
    
    jerk = np.sqrt((6*a3)**2)
    
    return [tf,jerk]

problem = Problem(1,2)
problem.types[:] = Real(3,20)
problem.directions = [-1,-1]
problem.function = cubicTraj

algorithm = NSGAII(problem)
algorithm.run(10000)

tf_opt = [s.objectives[0] for s in algorithm.result]
jerk_opt = [s.objectives[1] for s in algorithm.result]

plt.scatter(tf_opt,jerk_opt)
plt.show()

tf = 5.23705
jerk = 4.96