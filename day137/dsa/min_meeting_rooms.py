"""
DSA Problem: Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times, find the minimum number of meeting rooms required.
"""

def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)
    s = e = rooms = 0
    while s < len(intervals):
        if starts[s] < ends[e]:
            rooms += 1
            s += 1
        else:
            e += 1
            s += 1
    return rooms

if __name__ == "__main__":
    intervals = [[0,30],[5,10],[15,20]]
    print("Min meeting rooms:", min_meeting_rooms(intervals))  # Output: 2
