from src.task2 import Data_Types

'''
Arguments: none
Checks if the variables returned from Data_Types function are the correct datatypes
Return: Assertions
'''
def test_Data_Types():
    integer, flt, string, boolean = Data_Types()
    assert isinstance(integer, int) # Checks for integer (int)
    assert isinstance(flt, float)   # Checks for float (float)
    assert isinstance(string, str)  # Checks for string (str)
    assert isinstance(boolean, bool) # Checks for boolean (bool)

