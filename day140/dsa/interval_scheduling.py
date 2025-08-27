"""
DSA Problem: Interval Scheduling Maximization
Given a set of intervals, find the maximum number of non-overlapping intervals.
"""

def interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = float('-inf')
    for interval in intervals:
        if interval[0] >= end:
            count += 1
            end = interval[1]
    return count

if __name__ == "__main__":
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    print("Max non-overlapping intervals:", interval_scheduling(intervals))  # Output: 3
