"""
DSA Problem: House Robber
Given a list of non-negative integers representing the amount of money of each house, find the maximum amount of money you can rob tonight without alerting the police.
"""

def rob(nums):
    prev = curr = 0
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr

if __name__ == "__main__":
    nums = [1,2,3,1]
    print("Max rob:", rob(nums))  # Output: 4
