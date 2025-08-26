"""
DSA Problem: Binary Search
Given a sorted array and a target value, return the index if the target is found. If not, return -1.
"""

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9]
    target = 5
    print("Index:", binary_search(nums, target))  # Output: 2
