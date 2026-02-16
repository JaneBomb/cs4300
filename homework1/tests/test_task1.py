from src.task1 import Hello

'''
Arguments: capsys (for capturing printed outputs in terminal) (https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html)
Tests if the correct statement has been printed from the Hello function in task1
Return: Assert
'''
def test_Hello(capsys):
    Hello()
    output = capsys.readouterr()  # Captures the output
    assert output.out == "Hello, World!\n"    # Checks for correct output
