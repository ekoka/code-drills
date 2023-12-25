"""
LC 238: Product of an Array Except Self

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
# 59 - 16
# follow-up - 10 (> 1h)
def solution(nums):
    L = [1] * len(nums)
    R = [1] * len(nums)
    last_index  = len(nums) - 1
    for i in range(len(nums)):
        if i > 0:
            L[i] = L[i-1] * nums[i-1]
            j = last_index - i
            R[j] = R[j+1] * nums[j+1]
    for i in range(len(nums)):
        L[i] = L[i] * R[i]
    return L

# follow-up
def solution(nums):
    rv = [1] * len(nums)
    last_index  = len(nums) - 1
    left_running_product = 1
    for i in range(1, len(nums)):
        left_running_product *= nums[i-1]
        rv[i] = left_running_product
    right_running_product = 1
    for j in range(len(nums)-2, -1, -1):
        right_running_product *= nums[j+1]
        rv[j] = rv[j] * right_running_product
    return rv

def product(nums):
    N = len(nums)
    rv = [1] * N
    prefixes = [1] * N
    suffixes = [1] * N
    for i in range(1, len(prefixes)):
        prefixes[i] = prefixes[i-1] * nums[i-1]
        suffixes[N-i-1] = suffixes[N-i] * nums[N-i]
    for i in range(N):
        rv[i] = prefixes[i] * suffixes[i]
    return rv

def product(nums):
    N = len(nums)
    rv = [1] * N
    prefix = 1
    suffix = 1
    for i in range(1, N):
        prefix *= nums[i-1]
        suffix *= nums[N-i]
        rv[i] *= prefix
        rv[N-i-1] *= suffix
    return rv

def product(nums):
    N = len(nums)
    rv = [1] * N
    l,r = 1,1
    for i in range(N):
        rv[i] *= l
        rv[N-i-1] *= r
        l *= nums[i]
        r *= nums[N-i-1]
    return rv

nums = [1,2,3,4]
print(solution(nums))
print(product(nums))
#Output: [24,12,8,6]
nums = [-1,1,0,-3,3]
print(solution(nums))
print(product(nums))
#Output: [0,0,9,0,0]
