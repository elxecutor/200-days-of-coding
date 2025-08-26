"""
DSA Problem: Remove Duplicates from Sorted Array
Given a sorted array, remove the duplicates in-place such that each element appears only once and return the new length.
"""

def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

if __name__ == "__main__":
    nums = [1,1,2]
    print("New length:", remove_duplicates(nums))  # Output: 2
    nums = [0,0,1,1,1,2,2,3,3,4]
    print("New length:", remove_duplicates(nums))  # Output: 5
