"""
LC 056: Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.



Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104
"""
# 56
def merge(intervals):
    intervals.sort()
    rv = [intervals[0]]
    for i in range(1, len(intervals)):
        invl = intervals[i]
        merged = rv[-1]
        if merged[0] <= invl[0] and invl[0] <= merged[1]:
            merged[1] = max(invl[1], merged[1])
            continue
        if merged[0] <= invl[1] and invl[1] <= merged[1]:
            merged[0] = min(invl[0], merged[0])
            continue
        rv.append(invl)
    return rv

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
# Output: [[1,6],[8,10],[15,18]]

intervals = [[1,4],[4,5]]
print(merge(intervals))
# Output: [[1,5]]
