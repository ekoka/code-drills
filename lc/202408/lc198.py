"""
LC 198 : Houser Robber 

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

 

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 400
"""
def rob(nums):
    res = [0] * (nums+1)
    res[1] = nums[0]
    res[2] = nums[1]
    for i in range(3, nums+1):
        res[i] = max(res[i-2], res[i-3]) + nums[i-1]
    return res[-1]

def rob(nums):
    res = [0] * (nums+1)
    res[1] = nums[0]
    res[2] = nums[1]
    for i in range(3, nums+1):
        res[i] = max(res[i-2], res[i-3]) + nums[i-1]
    return res[-1]


def rob(nums):
    res = [0] * len(nums)
    res[0] = nums[0]
    res[1] = max(nums[1], nums[0])
    for i in range(2, nums):
        res[i] = max(res[i-2] + nums[i], res[i-1])
    return res[-1]
def rob(nums):
    res = [0] * len(nums)
    res[0] = nums[0]
    res[1] = max(nums[1], nums[0])
    for i in range(2, nums):
        res[i] = max(res[i-2] + nums[i], res[i-1])
    return res[-1]

def rob(nums):
    one = 0
    two = 0
    three = 0
    for i in range(len(nums)):
        curr = nums[i] + (one if one > two else two)
        one, two, three = two, three, curr
    return two if two > three else three

def rob(nums):
    one = 0
    two = 0
    three = 0
    for i in range(len(nums)):
        one, two, three = two, three, nums[i] + (one if one > two else two)
    return two if two > three else three


nums = [2,1,1,2]
print(rob(nums))
print(rob2(nums))
print(rob3(nums))
print(rob4(nums))
nums = [1,2,3,1]
print(rob(nums))
print(rob2(nums))
print(rob3(nums))
print(rob4(nums))
nums = [2,7,9,3,1]
print(rob(nums))
print(rob2(nums))
print(rob3(nums))
print(rob4(nums))
nums = [1,2]
print(rob(nums))
print(rob2(nums))
print(rob3(nums))
print(rob4(nums))
