"""
DSA Problem: Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""

def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
    return []

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print("Indices:", two_sum(nums, target))  # Output: [0, 1]
