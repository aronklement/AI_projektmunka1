# Write a function that returns the factorial of the given integer.

def factorial(number):
    fact = 1
    if number >= 0:
        for x in range(1, number + 1):
            fact *= x
        return fact
    else:
        return -1

print(factorial(4))