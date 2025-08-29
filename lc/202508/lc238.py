def product(nums):
    n = len(nums)
    prefix = [1] * n
    suffix = prefix[:]
    res = prefix[:]

    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]
    
    res[n-1] = prefix[n-1]
    for j in range(n-2, -1, -1):
        sufffix[j] = suffix[j+1] * nums[j+1]
        res[i] = prefix[j] * suffix[j]

    return res
