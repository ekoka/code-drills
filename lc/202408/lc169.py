# 30 - 43
"""
LC 169 Majority Element

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

 
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
def majority_element(nums):
    e = None
    c = 0
    for i in range(len(nums)):
        if e is None:
            e = nums[i]
            c = 1
        elif e==nums[i]:
            c += 1
        else:
            c -= 1
            if c==0:
                e = None
    return e

def majority_element(nums):
    e = None
    c = 0
    for n in nums:
        if e==n or c==0:
            e = n
            c += 1
        else:
            c -= 1
    return e
