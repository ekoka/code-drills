"""
LC 055 : Jump Game

You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 105
"""
# dp
def canjump(nums):
    N = len(nums)
    rv = [False] * N
    rv[N-1] = True
    for i in range(N-2, -1, -1):
        for j in range(i, i+nums[i]+1):
            if rv[j]:
                rv[i] = True
                break
    return rv[0]

def canjump(nums):
    canreach = len(nums)-1
    for i in range(canreach-1, -1, -1):
        if i+nums[i] >= canreach:
           canreach = i
    return canreach==0

print(canjump([2,3,1,1,4]))
# Output: true
print(canjump([3,2,1,0,4]))
# Output: false
