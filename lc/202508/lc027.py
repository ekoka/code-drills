# 10

def remove_element(nums, val):
    n = len(nums)
    i = 0
    j = 0
    while True:
        while i < n and nums[i]!=val:
            i += 1
        while j < n and nums[j]==val:
            j += 1
        if i < n and j < n:
            nums[i] = nums[j]
            nums[j] = '_'
        else:
            break
    return i + 1
