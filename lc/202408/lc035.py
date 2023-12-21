"""
# LC 035 : Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

- Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

- Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

- Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104
"""
# 35 - 42
def search_insert(nums, target):
    start = 0
    stop = len(nums)
    while start<stop:
        m = (start+stop)//2
        if nums[m]==target:
            return m
        if nums[m] < target:
            start = m+1
        else:
            stop = m
    return stop
