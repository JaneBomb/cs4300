from src.task4 import Calculate_Discount

'''
Arguments: none
Checks if the applied discounts are correct
Return: Assert
'''
def test_Calculate_Discount():
    assert Calculate_Discount(10, 100) == 10            # Integer
    assert Calculate_Discount(365, 12.2) == 44.53       # Decimal
    assert Calculate_Discount("orange", 1) == 1         # Non-numeric
