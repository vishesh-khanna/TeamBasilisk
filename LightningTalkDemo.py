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
    B = np.pi*(r**2)
    S = np.pi*r*sh
    T = B + S
    return [S,T]

problem = Problem(2,2)
problem.types[:] = [Real(4,10), Real(0,20)]
problem.function = objectiveFunc

algorithm = NSGAII(problem)
algorithm.run(1)

S_opt = [s.objectives[0] for s in algorithm.result]
T_opt = [s.objectives[1] for s in algorithm.result]

plt.scatter(S_opt, T_opt)
plt.xlabel('Surface Area')
plt.ylabel('Total Area')
plt.title('Offspring Population')
plt.show()

