# Install a library using pip if not already installed
# pip install numpy

import numpy as np
'''
Arguments: none
Creates a numpy array and mutiplies it by 2 (results in a different behaviour compared to default list/array)
Return: none (print statement)
'''
def NP_array():
    arr = np.array([[1, 2, 3], [4, 5, 6]])       # creates a 2x3 numpy array
    arr = arr * 2       # Multiplies the numpy array by 2
                        # Numpy = multiply each element by 2
                        # Default = print everything 2 times
    # Prints elements in array
    for i in arr:
        print(i, end="")        # Removes new line from each print statement