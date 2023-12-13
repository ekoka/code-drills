"""
LC 001: Two Sum
"""
# 46 - 05 (follow up solution)
def two_sum(nums, target):
    sorted_nums = sorted(nums)
    i = 0
    j = len(nums)-1
    while True:
        v = sorted_nums[i] + sorted_nums[j]
        if v > target:
            j -= 1
        elif v < target:
            i += 1
        else:
            break
    rv = []
    x,y = sorted_nums[j], sorted_nums[i]
    for i in range(len(nums)):
        if nums[i]==x:
            rv.append(i)
            x = None
        elif nums[i]==y:
            rv.append(i)
            y = None
        if len(rv)==2:
            break
    return rv

# less efficient
def two_sum(nums, target):
    indexes = {n:[] for n in nums} 
    for i in range(len(nums)):
        indexes[nums[i]].append(i)
    nums.sort()
    i = 0
    j = len(nums)-1
    while True:
        v = nums[i] + nums[j]
        if v > target:
            j -= 1
        elif v < target:
            i += 1
        else:
            # return first and last of possible sequence (for when it's the same number twice)
            return indexes[nums[i]][0], indexes[nums[j]][-1]
