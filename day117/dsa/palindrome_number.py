"""
DSA Problem: Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

def is_palindrome(x):
    s = str(x)
    return s == s[::-1]

if __name__ == "__main__":
    x = 121
    print("Is palindrome?", is_palindrome(x))  # Output: True
    x = -121
    print("Is palindrome?", is_palindrome(x))  # Output: False
