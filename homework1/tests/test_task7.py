import numpy as np
from src.task7 import NP_array

'''
Arguments: capsys
Checks if the correct array was printed
Return: Assert
'''
def test_NP_array(capsys):
    NP_array()
    output = capsys.readouterr()  # Captures the output
    assert output.out == "[2 4 6][ 8 10 12]"    # Checks for correct output

