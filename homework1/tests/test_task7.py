import numpy as np
from src.task7 import create_NP_array

'''
Arguments: none
Checks if the datatype is of type for np array
Return: Assert
'''
def test_create_NP_array():
    arr = create_NP_array()
    assert isinstance(arr, np.ndarray)        # Checks for np array datatype
                                              # ndarray class: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html
