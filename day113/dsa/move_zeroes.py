"""
DSA Problem: Move Zeroes
Given an array, move all zeroes to the end while maintaining the relative order of the non-zero elements.
"""

def move_zeroes(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    print("After moving zeroes:", move_zeroes(nums))  # Output: [1, 3, 12, 0, 0]
