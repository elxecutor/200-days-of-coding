"""
DSA Problem: Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""

def is_palindrome(s):
    filtered = ''.join(c.lower() for c in s if c.isalnum())
    return filtered == filtered[::-1]

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print("Is palindrome?", is_palindrome(s))  # Output: True
    s = "race a car"
    print("Is palindrome?", is_palindrome(s))  # Output: False
