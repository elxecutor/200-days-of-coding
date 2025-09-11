"""
DSA Problem: Jump Game
Given an array of non-negative integers, you are initially positioned at the first index. Each element represents your maximum jump length. Determine if you can reach the last index.
"""

def can_jump(nums):
    max_reach = 0
    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)
    return True

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print("Can jump?", can_jump(nums))  # Output: True
    nums = [3,2,1,0,4]
    print("Can jump?", can_jump(nums))  # Output: False
