"""
DSA Problem: Merge Two Sorted Arrays
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Assume nums1 has enough space to hold additional elements from nums2.
"""

def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge(nums1, m, nums2, n)
    print("Merged array:", nums1)  # Output: [1,2,2,3,5,6]
