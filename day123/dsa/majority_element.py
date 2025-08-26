"""
DSA Problem: Majority Element
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊n/2⌋ times.
"""

def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

if __name__ == "__main__":
    nums = [3,2,3]
    print("Majority element:", majority_element(nums))  # Output: 3
