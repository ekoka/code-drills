"""
LC 215: Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:

    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104
"""
# 46 - 56
def partition(arr, start, stop):
    if start==stop: return
    lo = hi = start
    pivot = stop-1
    def arr_swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    while hi < pivot:
        if arr[hi] < arr[pivot]:
            arr_swap(lo, hi)
            lo += 1
        hi += 1
    arr_swap(lo, pivot)
    return lo

# not very efficient if there are many identical values.
def kth_largest(nums, k):
    nums = list(nums)
    start = 0
    stop = len(nums)
    k = stop - k
    while start < stop:
        p = partition(nums, start, stop)
        if p==k:
            return nums[p]
        if k < p:
            stop = p
        else:
            start = p+1

import heapq
def kth_largest(nums, k):
    heap = []
    for i in range(k):
        heapq.heappush(heap, nums[i])
    for j in range(k, len(nums)):
        heapq.heappushpop(heap, nums[j])
    return heap[0]

nums = [3,2,1,5,6,4]; k = 2
print(kth_largest(nums, k))
# Output: 5

nums = [3,2,3,1,2,4,5,5,6]; k = 4
print(kth_largest(nums, k))
# Output: 4

nums = [3,2,1,5,6,4]; k = 1
print(kth_largest(nums, k))
# Output: 6

nums = [3,2,1,5,6,4]; k = 6
print(kth_largest(nums, k))
# Output: 1
