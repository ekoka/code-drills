"""
LC 027: Remove Element

https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150


"""
# 26 - 02
def remove_element(nums, val):
    i = 0
    j = len(nums)-1
    while i <= j:
        if j >= 0 and nums[j]==val:
            j -= 1
            continue
        if nums[i]==val:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
            i += 1
            continue
        i += 1
    return j + 1

def remove_element(nums, val):
    i = 0
    j = len(nums)-1
    while i <= j:
        if nums[j]==val:
            j -= 1
            continue
        if nums[i]==val:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        i += 1
    return j + 1

