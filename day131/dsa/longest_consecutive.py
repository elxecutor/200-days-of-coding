"""
DSA Problem: Longest Consecutive Sequence
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
"""

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            current = num
            streak = 1
            while current + 1 in num_set:
                current += 1
                streak += 1
            longest = max(longest, streak)
    return longest

if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print("Longest consecutive:", longest_consecutive(nums))  # Output: 4
