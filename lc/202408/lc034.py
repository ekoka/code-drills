"""
LC 034: Find First and Last Position in Sorted Array

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109
"""
# 07

# Find middle first, then find left, then find right.
# Mildly optimal.
def search_range(nums, target):
    i, j = 0, len(nums)
    mid = -1
    start = -1
    end = -1
    while i<j:
        m = (i+j)//2
        if nums[m]==target:
            mid = m
            break
        if nums[m] < target:
            i = m+1
        else:
            j = m
    if mid==-1: return [-1, -1]
    i, j = 0, mid
    while i<j:
        m = (i+j)//2
        if nums[m]==target:
            j = m
        else:
            i = m+1
    start = i
    i, j = mid, len(nums)
    while i<j:
        m = (i+j)//2
        if nums[m]==target:
            i = m+1
        else:
            j = m
    end = i-1
    return [start, end]

# Find left boundary first, then find right.
def search_range(nums, target):
    N = len(nums)
    i, j = 0, N
    while i<j:
        m = (i+j)//2
        if nums[m]>=target:
            j = m
        else:
            i = m+1
    if i==N or nums[i]!=target:
        return [-1, -1]
    start = i
    j = N
    while i<j:
        m = (i+j)//2
        if nums[m]==target:
            i = m+1
        elif nums[m] > target:
            j = m
    return [start, j-1]

def search_range(nums, target):
    N = len(nums)
    lo = 0
    hi = N

    while lo < hi:
        m = (lo+hi)//2
        if nums[m] < target:
            lo = m+1
        else:
            hi = m

    if lo==N or nums[lo]!=target:
        return -1,-1

    left = lo
    hi = N
    while lo < hi:
        m = (lo+hi)//2
        if nums[m] <= target:
            lo = m+1
        else:
            hi = m

    return left, hi-1


nums = [5,7,7,8,8,10]; target = 8
print(search_range(nums, target))
# Output: [3,4]

nums = [5,7,7,8,8,10]; target = 6
print(search_range(nums, target))
# Output: [-1,-1]

nums = []; target = 0
print(search_range(nums, target))
# Output: [-1,-1]
