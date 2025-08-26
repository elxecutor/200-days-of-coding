"""
DSA Problem: Erase Overlap Intervals
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""

def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    end = intervals[0][1]
    count = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
    return count

if __name__ == "__main__":
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    print("Erase overlap intervals:", erase_overlap_intervals(intervals))  # Output: 1
