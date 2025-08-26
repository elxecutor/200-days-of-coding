"""
DSA Problem: Contains Duplicate
Given an array of integers, find if the array contains any duplicates.
"""

def contains_duplicate(nums):
    return len(nums) != len(set(nums))

if __name__ == "__main__":
    nums = [1,2,3,1]
    print("Contains duplicate?", contains_duplicate(nums))  # Output: True
    nums = [1,2,3,4]
    print("Contains duplicate?", contains_duplicate(nums))  # Output: False
