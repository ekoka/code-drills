def maxsubarray(nums):
    total = nums[0]
    res = total
    for i in range(1, len(nums)):
        total = max(total+nums[i], 0)
        if total > res:
            res = total
    return res

def maxsubarray_divconq(nums):
    sums = {'cur': -float('inf'), 'max': -float('inf')}
    def proc(start, stop):
        if stop-start==1:
            sums['cur'] = max(nums[start], sums['cur'] + nums[start]) 
        else:
            proc(start, start + (stop-start)//2)
            proc(start + (stop-start)//2, stop)
        sums['max'] = max(sums['cur'], sums['max'])
    proc(0, len(nums))
    return sums['max']

nums = [-2,1,-3,4,-1,2,1,-5,4]
exp = 6
res1 = maxsubarray(nums)
res2 = maxsubarray_divconq(nums)
print(res1)
print(res2)
assert exp==res1==res2

nums = [1]
exp = 1
res1 = maxsubarray(nums)
res2 = maxsubarray_divconq(nums)
print(res1)
print(res2)
assert exp==res1==res2

nums = [5,4,-1,7,8]
exp = 23
res1 = maxsubarray(nums)
res2 = maxsubarray_divconq(nums)
print(res1)
print(res2)
assert exp==res1==res2
