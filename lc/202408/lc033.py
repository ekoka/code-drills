"""
LC 033: Search in Rotated Sorted Array

There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1



Constraints:

    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -104 <= target <= 104
"""
def search(nums, target):
    lo = 0
    hi = len(nums)

    while lo < hi:
        m = (lo+hi)//2

        if nums[m]==target:
            return m

        if nums[m] < target:
            if target <= nums[hi-1]:
                lo = m+1
            else: # if nums[hi-1] > target
                if nums[lo] <= nums[m]:
                    lo = m+1
                else: # if nums[lo] > nums[m]:
                    hi = m
            continue
        if target < nums[m]:
            if nums[lo] <= target:
                hi = m
            else: # if nums[lo] > target
                if nums[lo] <= nums[m]:
                    lo = m+1
                else: # nums[lo] > nums[m]
                    hi = m
    return -1

def search(nums, target):
    lo, hi = 0, len(nums)
    # find interval
    while nums[lo] > nums[hi-1]:
        m = (lo+hi)//2
        if nums[lo] <= nums[m]:
            if nums[lo] <= target and target <= nums[m]:
                hi = m+1
            else:
                lo = m+1
        else:
            if nums[m] <= target and target <= nums[hi-1]:
                lo = m
            else:
                hi = m
    # find item
    while lo<hi:
        m = (lo+hi)//2
        if nums[m]==target:
            return m
        if target < nums[m]:
            hi = m
        else: # if nums[m] < target
            lo = m+1
    return -1

def search(nums, target):
    lo = 0
    hi = len(nums)

    l = lo
    h = hi
    while nums[l] > nums[h-1]:
        m = (l+h)//2
        if nums[m-1] > nums[m]:
            l = m
        if nums[m] > nums[hi-1]:
            l = m+1
        elif nums[m] < nums[lo]:
            h = m

    if  l:
        if nums[l] <= target <= nums[hi-1]:
            lo = l
        else:
            hi = l

    while lo < hi:
        m = (lo+hi)//2
        if nums[m]==target:
            return m
        if nums[m] > target:
            hi = m  
        else:
            lo = m+1
    return -1

def search(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[lo]:
            if target < nums[mid] and target >= nums[lo]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if target <= nums[hi] and target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1




nums = [4,5,6,7,0,1,2]; target = 0
print(search(nums, target))
# Output: 4

nums = [4,5,6,7,0,1,2]; target = 3
print(search(nums, target))
# Output: -1

nums = [1]; target = 0
print(search(nums, target))
#Output: -1
