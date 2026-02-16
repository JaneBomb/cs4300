'''
Argument: Numerical values for dicount and original_price
Applies discount to the original price
Return: Returns the modified price
'''
def Calculate_Discount(discount, original_price):
    if isinstance(discount, int) or isinstance(discount, float):
        dicount = discount/100      # Converts to a decimal (percentages)
        return round(original_price * dicount, 2)       # Output rounds/formats to xx.xx if decimal
    else:
        return 1       # Error (not numerical value)
