"""
DSA Problem: Contains Nearby Duplicate
Given an array of integers and an integer k, return true if there are two distinct indices i and j such that nums[i] == nums[j] and abs(i - j) <= k.
"""

def contains_nearby_duplicate(nums, k):
    lookup = {}
    for i, num in enumerate(nums):
        if num in lookup and i - lookup[num] <= k:
            return True
        lookup[num] = i
    return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    k = 3
    print("Contains nearby duplicate?", contains_nearby_duplicate(nums, k))  # Output: True
    nums = [1,0,1,1]
    k = 1
    print("Contains nearby duplicate?", contains_nearby_duplicate(nums, k))  # Output: True
