# Write a function that checks whether the given string is a palindrome.

def is_palindrome(string):
    if string.lower() == string[-1::-1].lower():
        return True
    else:
        return False

print(is_palindrome('anna'))