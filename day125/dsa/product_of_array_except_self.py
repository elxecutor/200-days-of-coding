"""
DSA Problem: Product of Array Except Self
Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
"""

def product_except_self(nums):
    n = len(nums)
    output = [1] * n
    left = 1
    for i in range(n):
        output[i] = left
        left *= nums[i]
    right = 1
    for i in range(n-1, -1, -1):
        output[i] *= right
        right *= nums[i]
    return output

if __name__ == "__main__":
    nums = [1,2,3,4]
    print("Product except self:", product_except_self(nums))  # Output: [24,12,8,6]
