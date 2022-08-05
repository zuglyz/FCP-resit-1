# Author: Zara Shilakis


My repository consists of 4 main code files: odesolve.py, solveto.py, solveto_and_euler_rk4.py and numpy_and_graphs.py. Explanations for each file can be found below.

For all files, I utilized the input variable for users to write out their initial conditions to solve ODEs. I believe this is a more efficient and versatile way to use this algorithm rather than manually changing the value of individual variables.


odesolve.py

In the odesolve.py file, I have the basic algorithm to solve ODEs using either the euler method or the RK4 method. The euler method estimates the y-value based on a x-value, while the RK4 method estimates the x-value based on a y-value. I use for loops to calculate the values of x and y variables at each step. Each value is printed in the output in a table-like structure. The final values of x and y is printed at the bottom. For loops are a key tool used in all files of my repository.


solveto.py

In this file, I combined the euler method and the RK4 method into a single function. The user is able to choose which method to employ using the method input variable which will then call for the corresponding sub-function to run the method chosen.
The details of each sub-function (which are the euler and rk4 function defined in odesolve.py) are not included in this file. Thus, they must be imported at the beginning of the code to ensure that the code runs smoothly.
I did this by importing all functions from odesolve.py by using the asterick (*).


solveto_and_euler_rk4.py

This file is an extension of solveto.py. It is a visualization of how the algorithm would look if the euler and rk4 functions were defined within the same file as the solveto function. The solveto function, as mentioned above, calls either the euler function or the rk4 function depending on the input of the user. 
I defined the euler and rk4 functions above defining the solveto function within this file. 
By defining the euler and rk4 function within the same file, we aren't required to import them from odesolve.py. However, I uncommented the input variables part of the euler and rk4 algorithms to reduce repetition.
The inputs required directly correspond to the solveto function. 
The solveto function within this file acts the same as the solveto function in solveto.py.


numpy_and_graphs.py

This file contains edited versions of the euler and rk4 functions to incorporate numpy arrays in order for a plot to be produced. The functions act similarly to when either function is called. The only difference is that a scatterplot is produced to aid in visualization of the ODE. The graph is plotted with the x-value on the x-axis and the y-value on the y-axis.
I incorporated the numpy array into the for loops of each function so that the points would be automatically added to the numpy array every time they're calculated at each step. Once the for loop exits, the numpy array will consist of each set of x- and y-values which will then be plotted using matplotlib. 
Matplotlib and Numpy must both be imported before these functions can run.


png files

Finally, my repository also includes 4 png files which are screenshots of the outputs and graphs of my euler and rk4 functions from numpy_and_graphs.py. They act as examples of my code succeeding in producing x-value and y-value solutions to ODEs as well as plotting x- and y-values from each step into a scatterplot.
