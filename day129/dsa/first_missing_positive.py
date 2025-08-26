"""
DSA Problem: First Missing Positive
Given an unsorted integer array, find the smallest missing positive integer.
"""

def first_missing_positive(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
    for i in range(n):
        if nums[i] != i+1:
            return i+1
    return n+1

if __name__ == "__main__":
    nums = [1,2,0]
    print("First missing positive:", first_missing_positive(nums))  # Output: 3
    nums = [3,4,-1,1]
    print("First missing positive:", first_missing_positive(nums))  # Output: 2
