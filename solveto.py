from odesolve import *

# solveto function

# defining f

def f (x, t):
    return x

# initial conditions

print('Enter Initial Conditions:')
    
x0 = float(input('x0 = '))
t0 = float(input('t0 = '))
    
# Calculation Point
    
print('Enter calculation point: ')
tn = float(input('tn = '))
    
# Step Size
print('Enter step size: ')
h = float(input('Step Size = '))

# method
print('Choose method of calculation: ')
method = input('Method = ')

# solveto function

def solveto(f, x0, t0, tn, h, method):
    if method == 'Euler' or 'euler':
        # adjusting variables
        
        x0 = x0
        y0 = t0
        xn = tn
        n = h
        
        # calling the euler function
        
        euler_func = euler(x0, y0, xn, n)
        return euler_func
    
    if method == 'rk4' or 'RK4' or 'Rk4':
        #adjusting variables
        
        a0 = x0
        b0 = t0
        bc = xn
        c = h
        
        # calling the rk4 function
        
        rk4_func = rk4(a0, b0, bc, c)
        return rk4_func
    
    else:
        print('Choose either the Euler method or the RK4 method')
    

# calculating for x when t = tn; calling the solveto function

xn = solveto(f, x0, t0, tn, h, method)

# printing out the solution

print(xn)



