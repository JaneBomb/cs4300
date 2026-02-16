'''
Arguments: A number (int or float)
Identifies whether the passed in number is positive, negative, or zero
Return: String indicator for number
'''
def posNegZero(num):
    # Checks if the given number is positive, negative, or zero
    if(num > 0):
        return "Positive"
    elif(num < 0):
        return "Negative"
    elif(num == 0):
        return "Zero"
    else:
        return 1    # Returns error

'''
Arguments: none
Calculates the first 10 prime numbers
Return: none (prints output)
'''
def Primes():
    primes = [] 
    num = 2 
    while len(primes) < 10:     # Ensures that the first 10 prime numbers are calculated
        is_prime = True 
        for i in range(2, int(num**0.5) + 1):   # Checks if prime (prime numbers are not divisiable by anything, but itself and 1)
            if num % i == 0: 
                is_prime = False 
        # Appends to empty list if is a prime number
        if is_prime: primes.append(num) 
        num += 1 

    # Prints the first 10 prime numbers
    # Removes the default new line with ends=""
    print(primes, end="")

'''
Arguments: none
Sums numbers from 1 to 100 (1 + 2 + 3 + [...])
Return: The sum of all numbers
'''
def SumOf():
    sum = 0
    increment = 1
    limit = 100
    for i in range(limit):
        sum += increment
        increment +=1
    return sum

