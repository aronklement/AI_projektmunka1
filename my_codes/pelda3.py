# Write a function that returns a list containing words longer than 5 characters.

def longer_than_5(strings):
    long_strings = []
    for string in strings:
        if len(string) > 5:
            long_strings.append(string)
    return long_strings

print(longer_than_5(['hawthorn', 'louse', 'ball', 'football']))