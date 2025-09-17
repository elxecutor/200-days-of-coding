"""
DSA Problem: Intersection of Two Arrays
Given two arrays, return their intersection as a list of unique elements.
"""

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print("Intersection:", intersection(nums1, nums2))  # Output: [2]
