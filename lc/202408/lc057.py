"""
LC 057: Insert Interval

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the ith interval and `intervals` is sorted in ascending order by starti. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 105
    intervals is sorted by starti in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 105
"""
# 46
def insert(intervals, new_interval):
    inserted = []
    i = 0
    while intervals[i][0] <= new_interval[0]:
        inserted.append(intervals[i])
        i += 1
    inserted.append(new_interval)
    while i < len(intervals):
        inserted.append(intervals[i])
        i += 1
    rv = [inserted[0]]
    for i in range(1, len(inserted)):
        last = rv[-1]
        invl = inserted[i]
        if last[0] <= invl[0] <= last[1] or invl[0] <= last[1] <= invl[1]:
            last[0] = min(last[0], invl[0])
            last[1] = max(invl[1], last[1])
            continue
        rv.append(inserted[i])
    return rv


intervals = [[1,3],[6,9]]
new_interval = [2,5]
print(insert(intervals, new_interval))
# Output: [[1,5],[6,9]]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_interval = [4,8]
print(insert(intervals, new_interval))
# Output: [[1,2],[3,10],[12,16]]
