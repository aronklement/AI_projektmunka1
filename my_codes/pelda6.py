# Write a function that determines whether the given number is prime.

def is_prime(number):
    divisors = range(2, round(number ** (1 / 2)) + 1)
    if number >= 2:
        for x in divisors:
            if number % x == 0:
                return False
        return True
    else:
        return False

print(is_prime(3))