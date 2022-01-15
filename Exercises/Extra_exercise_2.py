# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 00:10:09 2022

@author: JAG
"""
"""
1. Rita en graf av funktionen f(x) = 2 sin(x) + 3 sin(2x) på intervallet −π ≤ x ≤ π i en figur.
Rita grafen g(x) = 8 sin(x) + 2 sin(2x) i samma figur. Använd samma x-värden.
"""
from numpy import linspace
from matplotlib.pyplot import plot
from math import sin, pi

x=linspace(-pi,pi)
f=2*sin(x)+3*sin(2*x)
g=8*sin(x)+2*sin(2*x)
plot(x,f)
plot(x,g)

