# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:11:53 2020

@authors: Nick Machak, Dominic Fascitelli, Vishesh Khanna
"""

from platypus import NSGAII, Problem, Real
import numpy as np
import matplotlib.pyplot as plt

def objectiveFunc(values):
    r = values[0]
    h = values[1]
    sh = (r**2 + h**2)**0.5
    S = np.pi*r*sh
    V = (np.pi**(r**2)*h)/3
    return [S,V]

problem = Problem(2,2)
problem.types[:] = [Real(0,2), Real(0,4)]
problem.directions = [-1,1]
problem.function = objectiveFunc

algorithm = NSGAII(problem)
algorithm.run(10000)

S_opt = [s.objectives[0] for s in algorithm.result]
V_opt = [s.objectives[1] for s in algorithm.result]

plt.scatter(S_opt, V_opt)
plt.xlabel('Surface Area')
plt.ylabel('Volume')
plt.title('Offspring Population')
plt.show()

