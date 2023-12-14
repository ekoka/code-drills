"""
LC 219 : Contains Duplicate II
"""
# 32 - 46 (solved, fairly efficient 39%)
def contains_nearby_dupe(nums, k):
    t = 0
    h = 0
    s = set()
    while h <= k and h < len(nums):
        if nums[h] in s:
            return True
        s.add(nums[h])
        h += 1

    while h < len(nums):
        s.remove(nums[t])
        if nums[h] in s:
            return True
        s.add(nums[h])
        t += 1
        h += 1
    return False

def contains_nearby_dupe(nums, k):
    if k >= len(nums):
        return len(set(nums)) < len(nums)
    t = 0
    h = 0
    s = {nums[i]:1 for i in range(k+1)}
    if len(s) < k+1: return True
    for i in range(k+1, len(nums)):
        s[nums[t]] -= 1
        s[nums[h]] += 1
        if s[nums[h]]==2: return True
        t += 1
        h += 1
    return False

# efficient (99%)
def contains_nearby_dupe(nums, k):
    if len(set(nums))==len(nums):
        return False
    d = {}
    for i in range(len(nums)):
        if nums[i] in d and i - d[nums[i]] <= k: 
            return True 
        d[nums[i]] = i
    return False
