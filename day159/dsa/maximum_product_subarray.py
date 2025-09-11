"""
DSA Problem: Maximum Product Subarray
Find the contiguous subarray within an array which has the largest product.
"""

def max_product(nums):
    max_prod = min_prod = result = nums[0]
    for num in nums[1:]:
        choices = (num, max_prod * num, min_prod * num)
        max_prod = max(choices)
        min_prod = min(choices)
        result = max(result, max_prod)
    return result

if __name__ == "__main__":
    nums = [2,3,-2,4]
    print("Max product subarray:", max_product(nums))  # Output: 6
