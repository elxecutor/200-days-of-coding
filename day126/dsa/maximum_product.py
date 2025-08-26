"""
DSA Problem: Maximum Product of Three Numbers
Given an integer array, find three numbers whose product is maximum and return the maximum product.
"""

def maximum_product(nums):
    nums.sort()
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

if __name__ == "__main__":
    nums = [1,2,3]
    print("Maximum product:", maximum_product(nums))  # Output: 6
    nums = [-10,-10,5,2]
    print("Maximum product:", maximum_product(nums))  # Output: 500
