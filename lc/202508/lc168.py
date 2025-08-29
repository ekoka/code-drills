def majority_element(nums):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
    el, cnt = (None, 0)
    for e, c in count.items():
        if c > cnt:
            el, cnt = e,c
    return el

def majority_element(nums):
    count = 0
    el = None
    for n in nums: 
        if count==0:
            el = n
        if el==n:
            count += 1 
        else:
            count -= 1
    return el
