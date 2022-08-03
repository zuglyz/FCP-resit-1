# odesolve.py
#
# Author: Zara Shilakis
# Date:   3rd August 2022
# Description: <insert description>

# Euler Method Code

# Function to be solved
def f(x,y):
    return x+y

# Defining variables

# x0 and y0 = Initial conditions
# xn = Calculation point
# n = Number of steps

# Function for the Euler Method

def euler(x0, y0, xn, n):  
    #Calculating the step size
    h = (xn-x0)/n
    
    print('\n------SOLUTION-------')
    print('-----------------------')
    print('x0\y0\slope\yn')
    print('-----------------------')
    
    for i in range(n):
        slope = f(x0,y0)
        yn = y0 + h*slope
        print(x0, y0, slope, yn)
        print('-----------------------')
        y0 = yn
        x0 = x0+h
       
    print(xn, yn)
    
# Inputs for Function

# Intial Conditions
print('Enter Initial Conditions:')

x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

# Calculation Point
print('Enter calculation point: ')
xn = float(input('xn = '))

# Steps
print('Enter number of steps: ')
step = int(input('Number of steps = '))

# Calling the Euler Method

# euler(x0, y0, xn, n)


# RK4 Method Code

def f(a, b):
    return a+b

# Defining variables

# a0 and b0 = Initial conditions
# an = Calculation point
# c = Number of steps

# RK4 Method

def rk4 (a0, b0, an, c):
    # Calculating the step size
    d = (an-a0)/c
    
    print('\n------SOLUTION-------')
    print('-----------------------')
    print('a0\b0\bn')
    print('-----------------------')
    
    # For loop to repeat the algorithm for all steps until desired result
    
    for j in range(c):
        k1 = f(a0, b0)
        k2 = f(a0 + k1 * d/2, b0 + d/2)
        k3 = f(a0 + k2 * d/2, b0 + d/2)
        k4 = f(x(n) + k3 * h, b0 + d)
        
        k = (k1 + 2 * k2 + 2 * k3 + k4)/6
        bn = b0 + k
        
        print(a0, b0, bn)
        print('-----------------------')
        b0 = bn
        a0 = a0 + h
       
    print(an, bn)
    
# Inputs for Function

# Intial Conditions
print('Enter Initial Conditions:')

a0 = float(input('a0 = '))
b0 = float(input('b0 = '))

# Calculation Point
print('Enter calculation point: ')
an = float(input('an = '))

# Steps
print('Enter number of steps: ')
steps = int(input('Number of steps = '))

# Calling the RK4 method

# rk4(a0, b0, an, steps)
    
        
        

def solveto(f, x1, t1, t2, hmax, method=euler):
    """Use many steps of method to get from x1,t1 to x2,t2"""
    pass


def odesolve(f, X0, t, hmax, method=euler):
    """Compute the solution at different values of t"""
    pass
