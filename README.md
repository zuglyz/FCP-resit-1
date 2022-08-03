SUBMISSION

Submit a zip file containing the git repository

Repository = odesolve
Submission = odesolve.zip

Inside the zip file:
  odesolve folder = all code files and the .git folder

Code files and .git folder:
  README.md = Explains what is in the repository
  odesolve.py = Main code for the assignment
  test_odesolve.py = Provided with the assignment
  Jupyter notebook = Shows how to import and use functions that are defined in odesolve.py


TASK

GOAL: Make functions to solve ODEs using the Euler method and the RK4 method

odesolve.py provides the function that you should write but is missing the function body

Using test_odesolve.py, we need to make sure the code passes the 6 tests



ODEs using Euler Method

Defined by the rule:
  x(n+1) = x(n) + f(x(n), t(n)) * h
  where h = stepsize

Euler function should look like this:

# e ul e r c h e c k . py
from o d e s ol v e import e u l e r
# D e fi n e s the RHS o f our ODE
d e f f ( x , t ) :
r e t u r n x
# I n i t i a l c o n d i t i o n s
t 0 = 1
x0 = 1
h = 0. 5
t 1 = t 0 + h
x1 = e u l e r ( f , x0 , t0 , h )
p r i n t ( ’ S ol vi n g the ODE dx/ dt = x ’ )
p r i n t ( ’ I n i t i a l c o n di ti o n x = ’ , x0 , ’ when t = ’ , t 0 )
p r i n t ( ’ One s t e p o f the Eule r method with a s t e p s i z e o f h = ’ , h )
p r i n t ( ’ Gives an e s tim a t e o f x = ’ , x1 , ’ when t = ’ , t 1 )



ODEs using RK4

1 step of the RK4 looks like:
  k1 = f(x(n), t(n))
  k2 = f(x(n) + k1 * h/2, t(n) + h/2)
  k3 = f(x(n) + k2 * h/2, t(n) + h/2)
  k4 = f(x(n) + k3 * h, t(n) + h)
  
  x(n+1) = x(n) + (k1 + 2k2 + 2k3 + k4) * h/6
  
Once the RK4 method is working, make a function = solveto

solveto = Used to make a number of steps with either the Euler/RK4 method

It should be possible to use the solveto function with either the Euler method of the RK4 method

x1 = s o l v e t o ( f , x0 , t0 , t1 , hmax , e u l e r ) # Uses Eule r method
x1 = s o l v e t o ( f , x0 , t0 , t1 , hmax , rk4 ) # Uses RK4 method
x1 = s o l v e t o ( f , x0 , t0 , t1 , hmax ) # Uses Eule r method



Using Numpy Arrays

All functions should be able to ork with numpy arrays

import numpy a s np
from o d e s ol v e import s o l v e t o
# D e fi n e s the RHS o f our ODE
d e f f (X, t ) :
x , y = X
dxdt = y
dydt = −x
r e t u r n np . a r r a y ( [ dxdt , dydt ] )
# I n i t i a l c o n d i t i o n s
t 0 = 0
x0 = 1
y0 = 0
X0 = np . a r r a y ( [ x0 , y0 ] )



odesolve

The purpose of this function is to give many different values of the solution for x suitable for a plot

import numpy a s np
import m a t pl o tli b . p y pl o t a s p l t
from o d e s ol v e import o d e s ol v e
# D e fi n e s the RHS o f our ODE
d e f f (X, t ) :
x , y = X
dxdt = y
dydt = −x
r e t u r n np . a r r a y ( [ dxdt , dydt ] )
# I n i t i a l c o n d i t i o n s
x0 = 1
y0 = 0
X0 = np . a r r a y ( [ x0 , y0 ] )
h = 0. 0 1 # max s t e p s i z e
t = np . l i n s p a c e ( 0 , 1 0 , 1 0 0 ) # time s t o pl o t the s o l u t i o n
Xt = o d e s ol v e ( f , X0, t , h )
# Use .T t o t r a n s p o s e the a r r a y
p l t . pl o t ( t , Xt .T)
p l t . s a v e f i g ( ’ shm . pd f ’ )
p l t . show ( )

Code and the plot should be included in the notebook.
odesolve should use the solveto function repeatedly in a loop to make a 2D array representing the solution
