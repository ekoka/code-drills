"""
LC 228 : Summary Ranges
"""
# 20 - 46 (100%)
# nums = sorted unique ints
def summary_ranges(nums):
    if not nums: return []
    if len(nums)==1: return [f"{nums[0]}"]
    nums.append(nums[0]-1)  # add boundary item (ensuring it's out of sequence)
    t = 0 # tail
    res = []
    for h in range(1, len(nums)+1): # head
        if nums[h]!=nums[h-1]+1:
            res.append(f"{nums[t]}" if nums[t]==nums[h-1] else f"{nums[t]}->{nums[h-1]}")
            t = h
    nums.pop()              # pop boundary item
    return res

