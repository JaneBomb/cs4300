from src.task6 import read_file
from pathlib import Path        # Use to ensure the file exists

'''
Arguments: none
Checks if the correct amount of words were counted in the passed in file
Return: Assert
'''
def test_read_file():
    path = Path("src/task6_read_me.txt")
    if path.exists():
        assert read_file(path) == 104        # Manually counted the words and got 104