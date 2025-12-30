# Write a function that returns the sum of even numbers in a list.

def even_sum(numbers):
    total = 0
    for x in numbers:
        if x % 2 == 0:
            total += x
    return total

print(even_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))