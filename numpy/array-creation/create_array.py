import numpy as np

#generate array from python list
python_list = [1, 2, 2.1, 8.342, 2.343]
array_from_python_list = np.array(python_list)

# generate 1D array containing all numbers from -2.0 to 2.0 with spacing 0.2
step = 0.2
arange_array = np.arange(-2.0, 2.2 + step, step=step)

# Generate 1D array with 11 evenly space values between 0.5 and 1.5
linspace_array = np.linspace(0.5, 1.5, 11)

# generate a python string from a character array
char_array = np.array('hello world', 'c')
