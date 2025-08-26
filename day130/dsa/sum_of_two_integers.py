"""
DSA Problem: Sum of Two Integers
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
"""

def get_sum(a, b):
    MASK = 0xFFFFFFFF
    MAX = 0x7FFFFFFF
    while b != 0:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
    return a if a <= MAX else ~(a ^ MASK)

if __name__ == "__main__":
    a, b = 1, 2
    print("Sum:", get_sum(a, b))  # Output: 3
    a, b = -2, 3
    print("Sum:", get_sum(a, b))  # Output: 1
