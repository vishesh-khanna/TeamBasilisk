# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 01:33:31 2020

@author: Nick Machak, Vishesh Khanna, Dominic Fascitelli
"""

from platypus import NSGAII, Problem, Real
import numpy as np
import matplotlib.pyplot as plt

class TrajectoryPlanning:

    def coefficents(self,order, theta0, thetaf,t0,tf):
        a3 = (-2/tf**3)*(thetaf - theta0)
        a2 = (3/tf**2)*(thetaf - theta0)
        a1 = 0
        a0 = theta0
        array = [a3,a2,a1,a0]
        return array
    
    
    def OptimalParetoPoint(self,ParetoPoints):
        #Plot the graph for ParetoFront
        #Select the optimal Pareto Point
        size = int(len(ParetoPoints)/2)
        print(size)
        ParetoPoint = ParetoPoints[size]
        print(ParetoPoint)
        print('Groot')
        return ParetoPoint
    
    def NSGAOperation(self,t0,theta0,thetaf):         
        def Traj1(values):
            tf_objective_values = values[0]
            a3 = (-2/tf_objective_values**3)*(thetaf - theta0)
            jerk = np.sqrt((6*a3)**2)
            return [tf_objective_values,jerk]

        problem = Problem(1,2)
        problem.types[:] = Real(t0+3,20)
        problem.directions = [-1,-1]
        problem.function = Traj1
        algorithm = NSGAII(problem)
        algorithm.run(2000)
        tf_opt = [s.objectives[0] for s in algorithm.result]
        jerk_opt = [s.objectives[1] for s in algorithm.result]
        
        return tf_opt,jerk_opt

Problem1 = TrajectoryPlanning()     
order = 3

path_points = [15,25,45,65,85]
theta0 = path_points[0]
thetaf = path_points[1]
t0 = 0.01
coefficients_via_points = []
for i in range(len(path_points)+1):
    tf_opt,jerk_opt = Problem1.NSGAOperation(t0,theta0,thetaf)
    ParetoPoints1 = np.c_[np.array(tf_opt),np.array(jerk_opt)]
    OptimalParetoPoint = Problem1.OptimalParetoPoint(ParetoPoints1)
    tf = OptimalParetoPoint[0]
    optimized_coefficients = Problem1.coefficents(order,theta0,thetaf,t0,tf)
    if i ==len(path_points)-1:
        break
    theta0 = thetaf
    thetaf = path_points[i+1]
    t0 = tf    
    coefficients_via_points.append(optimized_coefficients)
print(coefficients_via_points)
#Come out of for loop
#We have coefficients for polynomials between the via points
#    Plot the polynomial
#    Plot the graphs
