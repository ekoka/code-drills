"""
LC 918: Maximum Sum Circular Subarray

Given a circular integer array `nums` of length n, return the maximum possible sum of a non-empty subarray of `nums`.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.



Constraints:

    n == nums.length
    1 <= n <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104

"""
# 56
def maxsum_circular(nums):
    max_rv = maxsum(nums)
    if max_rv < 0:
        return max_rv
    return max(max_rv, sum(nums)-minsum(nums))


def maxsum(nums):
    running_sum = float('-inf')
    rv = running_sum
    for n in nums:
        running_sum = n + max(0, running_sum)
        rv = max(rv, running_sum)
    return rv

def minsum(nums):
    running_sum = float('inf')
    rv = running_sum
    for n in nums:
        running_sum = n + min(0, running_sum)
        rv = min(rv, running_sum)
    return rv

def maxsum_circular(nums):
    # same algorithm, single pass
    max_running_sum = float('-inf')
    max_rv = max_running_sum
    min_running_sum = float('inf')
    min_rv = min_running_sum
    for n in nums:
        max_running_sum = n + (0 if max_running_sum<0 else max_running_sum)
        max_rv = max_rv if max_rv>max_running_sum else max_running_sum
        min_running_sum = n + (0 if 0<min_running_sum else min_running_sum)
        min_rv = min_rv if min_rv < min_running_sum else min_running_sum
    min_max_rv = sum(nums)-min_rv
    return max_rv if max_rv < 0 else (max_rv if max_rv > min_max_rv else min_max_rv)


nums = [1,-2,3,-2]
print(maxsum_circular(nums))
# Output: 3

nums = [5,-3,5]
print(maxsum_circular(nums))
# Output: 10

nums = [-3,-2,-3]
print(maxsum_circular(nums))
# Output: -2

nums = [-3]
print(maxsum_circular(nums))
# Output: -3

nums = [-1,3,-3,9,-6,8,-5,-5,-6,10]
print(maxsum_circular(nums))
# Output: 20
