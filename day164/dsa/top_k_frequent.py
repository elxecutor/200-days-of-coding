"""
DSA Problem: Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.
"""

def top_k_frequent(nums, k):
    from collections import Counter
    return [item for item, _ in Counter(nums).most_common(k)]

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print("Top k frequent:", top_k_frequent(nums, k))  # Output: [1,2]
