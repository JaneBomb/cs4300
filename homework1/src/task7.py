# Install a library using pip if not already installed
# !pip install numpy
import numpy as np
'''
Arguments: none
Creates a numpy array
Return: The numpy array
'''
def create_NP_array():
    arr = np.array([[1, 2, 3], [4, 5, 6]])       # creates a 2x3 numpy array
    return arr