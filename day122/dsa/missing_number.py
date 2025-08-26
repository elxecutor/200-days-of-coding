"""
DSA Problem: Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""

def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

if __name__ == "__main__":
    nums = [3,0,1]
    print("Missing number:", missing_number(nums))  # Output: 2
