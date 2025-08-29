def rotate1(nums, k):
    n = len(nums)
    k %= n
    head = nums[n-k:]
    tail = nums[:n-k]
    nums[0:k] = head
    nums[k:] = tail

def rotate2(nums, k):
    n = len(nums)
    k %= n
    for _ in range(k):
        tmp = nums[0]
        for dest in range(1, n):
            orig = tmp
            tmp = nums[dest]
            nums[dest] = orig
        nums[0] = tmp

def rotate3(nums, k):
    n = len(nums)
    k %= n
    swivel(nums, 0, n)
    swivel(nums, 0, k)
    swivel(nums, k, n)
    return nums
        
def swivel(a, start, stop):
    lo = start
    hi = stop - 1
    while lo < hi:
        a[lo], a[hi] = a[hi], a[lo]
        lo += 1
        hi -= 1

def rotate4(nums, k):
    n = len(nums)
    k %= n
    nums.extend(nums)
    nums[:] = nums[n-k:n-k+n]

# ex 1
nums = [1,2,3,4,5,6,7]
k = 3
expected = [5,6,7,1,2,3,4]

res = rotate1(nums[:], k)
print(res)
assert res==expected

res = rotate2(nums[:], k)
print(res)
assert res==expected

res = rotate3(nums[:], k)
print(res)
assert res==expected

res = rotate4(nums[:], k)
print(res)
assert res==expected

# ex 2
nums = [-1,-100,3,99]
k = 2
expected = [3,99,-1,-100]

res = rotate1(nums[:], k)
print(res)
assert res==expected

res = rotate2(nums[:], k)
print(res)
assert res==expected

res = rotate3(nums[:], k)
print(res)
assert res==expected

res = rotate4(nums[:], k)
print(res)
assert res==expected
