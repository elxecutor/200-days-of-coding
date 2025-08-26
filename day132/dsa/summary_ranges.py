"""
DSA Problem: Summary Ranges
Given a sorted integer array without duplicates, return the summary of its ranges.
"""

def summary_ranges(nums):
    ranges = []
    i = 0
    while i < len(nums):
        start = nums[i]
        while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
            i += 1
        end = nums[i]
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{end}")
        i += 1
    return ranges

if __name__ == "__main__":
    nums = [0,1,2,4,5,7]
    print("Summary ranges:", summary_ranges(nums))  # Output: ['0->2', '4->5', '7']
