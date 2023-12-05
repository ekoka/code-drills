# 14 - 37 - 43

def remove_duplicates(nums):
    count = 0
    pre = nums[0]
    for i in range(1, len(nums)):
        if nums[i]==pre:
            nums[i] = None
            count += 1
        else:
            pre = nums[i]
    k = len(nums) - count
    i = 0
    j = 0
    while i < k:
        if nums[j] is None:
            j += 1
        else:
            nums[i] = nums[j]
            i += 1
            j += 1
    return k

def remove_duplicates(nums):
    dupe_count = 0
    dupe = None
    write = 0
    for read in range(len(nums)):
        if nums[read]==dupe:
            dupe_count += 1
        else:
            nums[write] = dupe = nums[read]
            write += 1
    return len(nums) - dupe_count
