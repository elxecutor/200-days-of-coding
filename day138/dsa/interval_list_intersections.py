"""
DSA Problem: Interval List Intersections
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order. Return their intersection.
"""

def interval_intersection(A, B):
    i = j = 0
    result = []
    while i < len(A) and j < len(B):
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])
        if lo <= hi:
            result.append([lo, hi])
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return result

if __name__ == "__main__":
    A = [[0,2],[5,10],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]
    print("Interval intersections:", interval_intersection(A, B))  # Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
