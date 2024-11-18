"""
LC 053 Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
# 15 - 24

def maxsubarraysum(nums):
    running_sum = float('-inf')
    running_subarray = []
    rv = float('-inf')
    for n in nums:
        if running_sum > 0:
            running_sum += n
            running_subarray.append(n)
        else:
            running_sum = n
            running_subarray = [n]
        if rv < running_sum:
            rv = running_sum
    return rv

def maxsubarraysum_divconq(nums):
    def dc(start, stop, cursum, curmax):
        if stop-start==1:
            cursum = max(nums[start], cursum + nums[start])
            if curmax < cursum:
                return cursum, cursum
            return cursum, curmax
        m = (stop + start)//2
        cursum, curmax = dc(start, m, cursum, curmax)
        return dc(m, stop, cursum, curmax)
    _, rv = dc(0, len(nums), float('-inf'), float('-inf'))
    return rv

def maxsubarraysum(nums):
    n, pre = len(nums), list(nums)
    for i in range(1, n): pre[i] += max(pre[i-1], 0)
    return max(pre)

def maxSubArray(self, nums):
    pre, suf = [*nums], [*nums]
    for i in range(1, len(nums)):       pre[i] += max(0, pre[i-1])
    for i in range(len(nums)-2,-1,-1):  suf[i] += max(0, suf[i+1])
    def maxSubArray(A, L, R):
        if L == R: return A[L]
        mid = (L + R) // 2
        return max(maxSubArray(A, L, mid), maxSubArray(A, mid+1, R), pre[mid] + suf[mid+1])
    return maxSubArray(nums, 0, len(nums)-1)

def maxSubArray(nums):
    pre = [*nums]
    for i in range(1, len(nums)): pre[i] += max(0, pre[i-1])
    return max(pre)

def maxSubArray(nums):
    pre = nums[0]
    rv = pre
    for i in range(1, len(nums)):
        pre = nums[i] + max(pre, 0)
        if rv < pre:
            rv = pre
    return rv

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxsubarraysum(nums))
print(maxSubArray(nums))
print(maxsubarraysum_divconq(nums))
# Output: 6


nums = [1]
print(maxsubarraysum(nums))
print(maxSubArray(nums))
print(maxsubarraysum_divconq(nums))
# Output: 1

nums = [5,4,-1,7,8]
print(maxsubarraysum(nums))
print(maxSubArray(nums))
print(maxsubarraysum_divconq(nums))
#Output: 23
