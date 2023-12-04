"""
LC 088 : Merge Sorted Array

"""
# 37
def solution(nums1, nums2, m, n):
    i = m+n
    while n:
        if m and nums1[m-1] > nums2[n-1]:
            nums1[i-1] = nums1[m-1]
            m -= 1
        else:
            nums1[i-1] = nums2[n-1]
            n -= 1
        i -= 1


