"""
LC 300 : Longest Increasing Subsequence

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:

    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""

def solution1(nums):
    length = [1] * len(nums)
    rv = 1
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] >= nums[i]: 
                continue
            if length[i] < length[j] + 1:
                length[i] = length[j] + 1
        rv = max(rv, length[i])
    return rv

# ----------------
# Patience sorting: 
# https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf
def solution2(nums):
    stacks = [[]]
    for n in nums:
        stack = None
        for s in stacks:
            if len(s)==0 or s[-1]>=n:
                stack = s 
                break
        if stack is None:
            stacks.append([n])
        else:
            stack.append(n)
    return len(stacks)

# Notice that we only care about the last item on each stack. So we might as well just track the items rather than the stacks.
def solution3(nums):
    items = []
    for n in nums:
        j = None
        for i in range(len(items)):
            if items[i]>=n:
                j = i
                break
        if j is None:
            items.append(n)
        else:
            items[j] = n
    return len(items)

# The looping over items is essentially a lookup for the first item that is greater or equal to n. If nums is a small collection looping over items is fine. But if not, binary search is better.

from bisect import bisect_left
def solution4(nums):
    items = []
    for n in nums:
        i = bisect_left(items, n)
        if i==len(items):
            items.append(n)
        else:
            items[i] = n
    return len(items)
