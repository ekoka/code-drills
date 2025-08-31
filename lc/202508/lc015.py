# good performance
def three_sum(nums):
    nums.sort()
    res = []
    n = len(nums)
    i = 0
    for i in range(n-2):
        if 0 < nums[i]: break
        if i > 0 and nums[i-1]==nums[i]: continue
        j = i+1
        k = n-1
        v = -nums[i]
        while j < k:
            if j > i+1 and nums[j]==nums[j-1]:
                # we don't do this for k because we only decrement k 
                # when v < nums[j] + nums[k] and if nums[k]==nums[k+1]
                # then the decrement condition continues to apply.
                # whereas we increment j both when v == nums[j] + nums[k]
                # and v > nums[j] + nums[k]
                j+=1
                continue
            if v==nums[j] + nums[k]:
                res.append((nums[i], nums[j], nums[k]))
                j += 1
                continue
            while j < k and v > nums[j] + nums[k]: # increase j
                j += 1
            if v < nums[j]: break # might not make much of a difference
            while j < k and v < nums[j] + nums[k]: # decrease k
                k -= 1
    return res
