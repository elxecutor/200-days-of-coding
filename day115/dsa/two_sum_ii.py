"""
DSA Problem: Two Sum II - Input Array Is Sorted
Given a sorted array of integers, find two numbers such that they add up to a specific target number. Return their indices (1-indexed).
"""

def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []

if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    print("Indices:", two_sum(numbers, target))  # Output: [1, 2]
