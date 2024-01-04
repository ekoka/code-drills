"""
LC 452: Minimum Number of Arrows to Burst Balloons

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [xstart, xend]` denotes a balloon whose horizontal diameter stretches between `xstart` and `xend`. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if `xstart <= x <= xend`. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

Constraints:

    1 <= points.length <= 105
    points[i].length == 2
    -231 <= xstart < xend <= 231 - 1
"""
# 22

def solution(points):
    points.sort()
    def helper(cur, i, acc):
        if i >= len(points):
            return acc
        nxt = points[i]
        if cur[1] < nxt[0]:
            cur = nxt
            acc += 1
        else:
            cur[1] = min(cur[1], nxt[1])
        return helper(cur, i+1, acc)
    return helper(points[0], 0, 1)

def solution(points):
    points.sort()
    i = 0
    cur = points[i]
    rv = 1
    for nxt in points:
        if cur[1] < nxt[0]:
            cur = nxt
            rv += 1
            continue
        cur[1] = min(cur[1], nxt[1])
    return rv

"""
If we sort intervals by their ending values, the earlier intervals that intersect with their later counterparts define the entire subset's intersection (i.e. the subset of all intervals that intersect with the earlier interval).
"""

def solution(points):
    points.sort(key=lambda p: p[1])
    cur = points[0]
    count = 1
    for nxt in points:
        if nxt[0] <= cur[1]: continue
        cur = nxt
        count += 1
    return count


points = [[10,16],[2,8],[1,6],[7,12]]
print(solution(points))
# Output: 2

points = [[1,2],[3,4],[5,6],[7,8]]
print(solution(points))
# Output: 4

points = [[1,2],[2,3],[3,4],[4,5]]
print(solution(points))
# Output: 2

points = [[1,2]]
print(solution(points))
# Output: 1

points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
print(solution(points))
# Output: 2
