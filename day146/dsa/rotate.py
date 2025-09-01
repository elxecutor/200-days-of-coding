"""
DSA Problem: Rotate Array
Given an array, rotate the array to the right by k steps.
"""

def rotate(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    print("Rotated array:", rotate(nums, k))  # Output: [5,6,7,1,2,3,4]
