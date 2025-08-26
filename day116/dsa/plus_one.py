"""
DSA Problem: Plus One
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
"""

def plus_one(digits):
    n = len(digits)
    for i in range(n-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

if __name__ == "__main__":
    digits = [1,2,3]
    print("Result:", plus_one(digits))  # Output: [1,2,4]
    digits = [9,9,9]
    print("Result:", plus_one(digits))  # Output: [1,0,0,0]
