"""
LC 209: Minimum Size Subarray Sum

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:

    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

# Strickly sliding window

def sliding_window_prefix_sum(nums, target):
    rv = float('inf')
    running_sum = 0
    j = 0
    for i in range(len(nums)):
        running_sum += nums[i]
        if running_sum < target: continue
        while running_sum >= target:
            if j==i: return 1
            if rv > i+1-j:
                rv = i+1-j
            running_sum -= nums[j]
            j += 1
    if rv < float('inf'):
        return rv
    return 0

# Brute force
def brute_force(nums, target):
    def is_valid_size(size):
        i = 0
        j = 0
        total = 0
        while i < size-1: # fill window up to but not including last position
            total += nums[i]
        while i < len(nums): 
            total += nums[i]
            if total >= target:
                return True
            total -= nums[j]
            j += 1
        return False
    for size in range(1, len(nums)+1):
        if is_valid_size(size):
            return size
    return 0

# Binary search solution
def search_min_size(nums, target):
    lo = 1                     # minimum possible size.
    hi = len(nums) + 1         # 1 value past maximum size (i.e. out of range).
    res = 0
    while lo < hi:             # begin binary search
        test_size = (lo + hi)//2
        if window_size_is_possible(test_size, nums, target):
            res = test_size
            hi = test_size     # reduce hi to current test_size, excluding it from search range.
        else:
            lo = test_size+1   # increase lo, +1 ensures not stuck in endless loop, when hi-lo <= 1.
    return res

def window_size_is_possible(window_size, nums, target):
    i = 0
    running_sum = 0
    for j in range(window_size-1):  # fill the window up to, but not including, last item
        running_sum += nums[j]
    for j in range(window_size-1, len(nums)):
        running_sum += nums[j]      # add one item to window's head
        if running_sum >= target:   # check if window is now valid
            return True
        running_sum -= nums[i]      # remove one item from window's tail (fifo)
        i += 1
    return False
