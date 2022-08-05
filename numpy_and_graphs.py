# Author: Zara Shilakis




# Euler Method including Numpy Arrays and Scatterplot

import numpy as np
import matplotlib.pyplot as plt

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
    
    # Make a numpy array
    
    x = np.array([x0])
    y = np.array([y0])
    
    for i in range(h+1):
        slope = float(f(x0,y0))
        yn = float(y0 + n * slope)
        
        # Print Table
        
        print('%.4f\t%.4f\t%0.4f\t%.4f'% (x0, y0, slope, yn))
        print('----------------------------')
        
        # Next Round Variable Values
        
        y0 = yn
        x0 = x0 + n
        
        # Add variables to numpy array
        
        add_x = np.array([x0])
        add_y = np.array([y0])
        
        x = np.column_stack((x, add_x))
        y = np.column_stack((y, add_y))
        
    
    yn = y0 - (n * slope)
    # return xn, yn
    
    # printing solutions
    
    print("xn = ", xn)
    print("yn = ", yn)
    
    # Make a plot
    
    plt.scatter(x, y)
    plt.savefig('plot.pdf')
    plt.show()
    

# Calling the Euler Method

euler(x0, y0, xn, n)
