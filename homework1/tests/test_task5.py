from src.task5 import Favorite_Books, Student_Database

'''
Arguments: capsys (for printed outputs)
Checks if the correct data (only book titles) was printed
Return: Assert
'''
def test_Favorite_Books(capsys):
    Favorite_Books()
    output = capsys.readouterr()
    assert output.out == "The Glass Castle, The Kite Runner, Book 3"

'''
Arguments: none
Checks if the data in a dictoinary is the correct data type
Return: Assert
'''
def test_Student_Database():
    data = Student_Database()
    keys = data.keys()
    value = data.values()

    # Checks that all keys are strings (names)
    for i in keys:
        assert isinstance(i, str)
    
    # Checks that all values are ints (IDs)
    for i in value:
        assert isinstance(i, int)