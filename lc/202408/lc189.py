"""
LC 189 : Rotate Array

Given an integer array `nums`, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:

    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
"""
# 28
def rotate_flip(nums, k):
    N = len(nums)
    k = k % N
    flip(nums, 0, N)
    flip(nums, 0, k)
    flip(nums, k, N)

def flip(nums, start, stop):
    while stop-start>1:
        array_swap(nums, start, stop-1)
        start += 1
        stop -= 1

def array_swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def rotate(nums, k):
    N = len(nums)
    k %= N
    offset = N-k
    i = 0
    j = offset
    rv = [None] * N
    while j < N:
        rv[i] = nums[j]
        i += 1
        j += 1
    j = 0
    while j < offset:
        rv[i] = nums[j]
        i += 1
        j += 1
    for i in range(len(rv)):
        nums[i] = rv[i]

def rotate_concat(nums, k):
    cpy = nums + nums
    k = len(nums)-k
    for i in range(len(nums)):
        nums[i] = cpy[k]
        k += 1

nums = [1,2,3,4,5,6,7]; k = 3
rotate_flip(nums, k)
print(nums)
nums = [1,2,3,4,5,6,7]; k = 3
rotate_concat(nums, k)
print(nums)
nums = [1,2,3,4,5,6,7]; k = 3
rotate(nums, k)
print(nums)
# Output: [5,6,7,1,2,3,4]

nums = [-1,-100,3,99]; k = 2
rotate_flip(nums, k)
print(nums)
nums = [-1,-100,3,99]; k = 2
rotate_concat(nums, k)
print(nums)
nums = [-1,-100,3,99]; k = 2
rotate(nums, k)
print(nums)
# Output: [3,99,-1,-100]
