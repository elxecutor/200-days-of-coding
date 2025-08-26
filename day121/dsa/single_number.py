"""
DSA Problem: Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

if __name__ == "__main__":
    nums = [4,1,2,1,2]
    print("Single number:", single_number(nums))  # Output: 4
