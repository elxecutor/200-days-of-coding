"""
DSA Problem: Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

def is_anagram(s, t):
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print("Is anagram?", is_anagram(s, t))  # Output: True
    s = "rat"
    t = "car"
    print("Is anagram?", is_anagram(s, t))  # Output: False
