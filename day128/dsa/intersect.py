"""
DSA Problem: Intersection of Two Arrays II
Given two arrays, return an array of their intersection including duplicate elements.
"""

def intersect(nums1, nums2):
    from collections import Counter
    c1, c2 = Counter(nums1), Counter(nums2)
    result = []
    for num in c1:
        result += [num] * min(c1[num], c2.get(num, 0))
    return result

if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print("Intersection:", intersect(nums1, nums2))  # Output: [2,2]
