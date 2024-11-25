"""
LC 004: Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

"""
def find_median(nums1, nums2):
    N = len(nums1) + len(nums2)
    k1 = find_kth(nums1, nums2, N//2)
    if N % 2: return k1
    k2 = find_kth(nums1, nums2, N//2 - 1)
    return (k1+k2)/2

def find_kth(nums1, nums2, k):
    while nums1 and nums2:
        m1 = len(nums1)//2
        m2 = len(nums2)//2
        m = m1+m2
        v1 = nums1[m1]
        v2 = nums2[m2]
        if k==m:
            if v1==v2: return v1 
            if v1 < v2:
                nums1 = nums1[m1:]
                nums2 = nums2[:m2]
                k -= m1
            else:
                nums1 = nums1[:m1]
                nums2 = nums2[m2:]
                k -= m2

        elif k < m:
            if v1 < v2:
                nums2 = nums2[:m2]
            else:
                nums1 = nums1[:m1]
        
        else: #if k > (m1+m2):
            if v1 < v2:
                nums1 = nums1[m1+1:]
                k -= m1+1
            else:
                nums2 = nums2[m2+1:]
                k -= m2+1
    
    if not nums1: return nums2[k]
    if not nums2: return nums1[k]

def find_kth(nums1, nums2, k):
    lo1, hi1 = 0, len(nums1)
    lo2, hi2 = 0, len(nums2)
    while lo1<hi1 and lo2<hi2:
        m1 = (lo1+hi1)//2
        m2 = (lo2+hi2)//2
        m = m1+m2
        v1 = nums1[m1]
        v2 = nums2[m2]
        if k==m:
            if v1==v2: return v1 
            if v1 < v2:
                lo1 = m1
                hi2 = m2
            else:
                hi1 = m1
                lo2 = m2
        elif k < m:
            if v1 < v2:
                hi2 = m2
            else:
                hi1 = m1
        else: #if k > (m1+m2):
            if v1 < v2:
                lo1 = m1+1
            else:
                lo2 = m2+1
    if lo1==hi1: return nums2[k-hi1]
    if lo2==hi2: return nums1[k-hi2]
