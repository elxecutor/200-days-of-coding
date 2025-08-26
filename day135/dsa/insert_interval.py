"""
DSA Problem: Insert Interval
Given a set of non-overlapping intervals and a new interval, insert the new interval into the intervals (merge if necessary).
"""

def insert(intervals, new_interval):
    result = []
    for interval in intervals:
        if interval[1] < new_interval[0]:
            result.append(interval)
        elif interval[0] > new_interval[1]:
            result.append(new_interval)
            new_interval = interval
        else:
            new_interval[0] = min(new_interval[0], interval[0])
            new_interval[1] = max(new_interval[1], interval[1])
    result.append(new_interval)
    return result

if __name__ == "__main__":
    intervals = [[1,3],[6,9]]
    new_interval = [2,5]
    print("Inserted intervals:", insert(intervals, new_interval))  # Output: [[1,5],[6,9]]
