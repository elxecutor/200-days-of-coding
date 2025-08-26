"""
DSA Problem: Contains Duplicate III
Given an array of integers, find out whether there are two distinct indices i and j such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
"""

def contains_duplicate_iii(nums, k, t):
    if t < 0:
        return False
    bucket = {}
    w = t + 1
    for i, num in enumerate(nums):
        m = num // w
        if m in bucket:
            return True
        if m - 1 in bucket and abs(num - bucket[m - 1]) < w:
            return True
        if m + 1 in bucket and abs(num - bucket[m + 1]) < w:
            return True
        bucket[m] = num
        if i >= k:
            del bucket[nums[i - k] // w]
    return False

if __name__ == "__main__":
    nums = [1,5,9,1,5,9]
    k = 2
    t = 3
    print("Contains duplicate III?", contains_duplicate_iii(nums, k, t))  # Output: False
