"""
DSA Problem: Maximum Subarray
Find the contiguous subarray with the largest sum.
"""

def max_sub_array(nums):
    max_sum = curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print("Max subarray sum:", max_sub_array(nums))  # Output: 6
