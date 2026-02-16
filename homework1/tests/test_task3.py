from src.task3 import posNegZero, Primes, SumOf

'''
Arguments: none
Passes a number into task3_1 and checks for positive, negative, zero validity
Return: Assert
'''
def test_posNegZero():
    assert posNegZero(1) == "Positive"
    assert posNegZero(-1) == "Negative"
    assert posNegZero(0) == "Zero"

'''
Arguments: capsys (for capturing output)
Checks for the first 10 prime numbers
Return: Assert
'''
def test_Primes(capsys):
    expected_output = "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]"
    Primes()
    output = capsys.readouterr()  # Captures the output
    assert output.out == expected_output    # Checks for correct output

'''
Arguments: none
Checks for the sum of numbers from 1 to 100
Return: assert
'''
def SumOf():
    output = SumOf()
    assert output == 5050