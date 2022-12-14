# odesolve.py
#
# Author: Zara Shilakis
# Date:   3rd August 2022
# Description: <insert description>

# Euler Method Code

# Function to be solved
def f(x,y):
    return x+y

# Euler's rule

# x(n+1) = x(n) + f(x(n), t(n)) * h
#   where h = stepsize

# Defining variables

# x0 and y0 = Initial conditions
# xn = Calculation point
# n = Number of steps

# Inputs for Function
    
# Intial Conditions
    
print('Enter Initial Conditions:')
    
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))
    
# Calculation Point
    
print('Enter calculation point: ')
xn = float(input('xn = '))
    
# Step Size
print('Enter step size: ')
n = float(input('Step Size = '))


# Function for the Euler Method

def euler(x0, y0, xn, n):  
    # Calculating the number of steps
    h = int((xn-x0)/n)
    
    print('\n----------SOLUTION----------')
    print('----------------------------')
    print('x0, y0, slope, yn')
    print('----------------------------')
    
    for i in range(h+1):
        slope = float(f(x0,y0))
        yn = y0 + n * slope
        
        # Print Table
        
        print('%.4f\t%.4f\t%0.4f\t%.4f'% (x0, y0, slope, yn))
        print('----------------------------')
        
        # Next Round Variable Values
        
        y0 = yn
        x0 = x0 + n
    
    yn = y0 - (n * slope)
    
    # printing the solution
    
    print("xn = ", xn)
    print("yn = ", yn)
    

# Calling the Euler Method

euler(x0, y0, xn, n)






# RK4 Method Code

def f(a, b):
    return a+b


# Defining variables

# a0 and b0 = Initial conditions
# an = Calculation point
# c = Number of steps


# Inputs for Function

# Intial Conditions
print('Enter Initial Conditions:')

a0 = float(input('a0 = '))
b0 = float(input('b0 = '))

# Step Size
print('Enter step size: ')
c = float(input('Step Size = '))

# Calculation Point
print('Enter calculation point: ')
bc = float(input('bc = '))


# RK4 Method

def rk4 (a0, b0, bc, c):
    # Number of Steps
    d = int((bc - b0)/c)

    print('\n------SOLUTION-------')
    print('-----------------------')
    print('a0, b0, ac')
    print('-----------------------')
    
    # For loop to repeat the algorithm for all steps until desired result
    
    for j in range(0, d+1):
        k1 = f(a0, b0)
        k2 = f(a0 + (k1 * (c/2)), b0 + (c/2))
        k3 = f(a0 + (k2 * (c/2)), b0 + (c/2))
        k4 = f(a0 + k3 * c, b0 + c)
        
        k = ((k1 + 2 * k2 + 2 * k3 + k4) * (c/6))
        ac = a0 + k
        
        
        print(a0, b0, ac)
        print('-----------------------')
        
        # Next Round in the Loop
        
        a0 = ac
        b0 = b0 + c
       
    print("a = ", a0 - k)
    print("b = ", bc)


    
# Calling the RK4 method

rk4(a0, b0, bc, c)


