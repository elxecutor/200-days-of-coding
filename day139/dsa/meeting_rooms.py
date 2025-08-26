"""
DSA Problem: Meeting Rooms
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings.
"""

def can_attend_meetings(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True

if __name__ == "__main__":
    intervals = [[0,30],[5,10],[15,20]]
    print("Can attend all meetings?", can_attend_meetings(intervals))  # Output: False
    intervals = [[7,10],[2,4]]
    print("Can attend all meetings?", can_attend_meetings(intervals))  # Output: True
