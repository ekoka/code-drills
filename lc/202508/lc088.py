# 43
def merge_sorted_array(nums1, nums2, m, n):
    n = (m + n) - 1
    n1 = m - 1
    n2 = n - 1
    while n1 > -1 and n2 > -1:
        if nums1[n1] > nums2[n2]:
            nums1[n] = nums1[n1]
            n1 -= 1
        else:
            nums1[n] = nums2[n2]
            n2 -= 1
        n -= 1
    while n2 > -1:
        nums1[n] = nums2[n2]
        n2 -= 1
        n -= 1
