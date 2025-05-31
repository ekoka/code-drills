"""
# 1509 Minimum Diff Between Largest and Smallest in Three Moves
You are given an integer array nums.
In one move, you can choose one element of nums and change it to any value.
Return the minimum difference between the largest and smallest value of nums after performing at most three moves.
"""

def maxvalues(array, K):
    rv = [None] * K
    for v in array:
        insertmax(rv, v)
    return rv

def minvalues(array, K):
    rv = [None] * K
    for v in array:
        insertmin(rv, v)
    return rv

def insertmin(array, value):
    for i, v in enumerate(array):
        if v is None:
            array[i] = value
            return
        if v > value:
            shift_right(array, i)
            array[i] = value

def insertmax(array, value):
    for i, v in enumerate(array):
        if v is None:
            array[i] = value
            return
        if v < value:
            shift_right(array, i)
            array[i] = value

def shift_right(array, i):
    j = len(array) - 1
    while i < j:
        array[j] = array[j-1]
        j -= 1

def solution_minmaxvals(nums):
    moves = 3
    if moves >= len(nums):
        return 0
    max4 = maxvalues(nums, moves+1)
    min4 = minvalues(nums, moves+1)
    rv = float('inf')
    i = 0
    j = moves
    while i <= j:
        rv = min(rv, max4[i]-min4[j-i])
        i += 1
    return rv

def solution(nums):
    nums.sort()
    return helper(nums, 0, len(nums), 3)

def helper(nums, start, stop, moves):
    if stop - start <= 0:
        return 0
    if moves==0:
        return nums[stop-1] - nums[start]
    left = helper(nums, start+1, stop, moves-1)
    right = helper(nums, start, stop-1, moves-1)
    return min(left, right)

#def solution_iter(nums):
#    nums.sort()
#    stack = [(0, len(nums), 3)]
#    rv = float('inf')
#    while stack:
#        start, stop, moves = stack.pop()
#        if stop - start <= 0:
#            return 0
#        if moves==0:
#            rv = min(rv, nums[stop-1] - nums[start])
#            continue
#        stack.append((start+1, stop, moves-1))
#        stack.append((start, stop-1, moves-1))
#    return rv
import heapq
def solution_heap(nums):
    if len(nums) <= 4:
        return 0
    nlargest = heapq.nlargest(4, nums)
    nsmallest = heapq.nsmallest(4, nums)
    rv = float('inf')
    i = 0
    for i in range(4):
        k = 3 - i
        test = nlargest[i] - nsmallest[k]
        rv = rv if rv < test else test
    return rv

def solution_iter(nums):
    if len(nums) <= 4:
        return 0
    nums.sort()
    rv = float('inf')
    i = 0
    j = len(nums) - 1
    for i in range(3):
        k = 3 - i
        rv = min(rv, nums[j-k] - nums[i])
    return rv

nums = [5,3,2,4]
print(solution(nums))
print(solution_iter(nums))
print(solution_minmaxvals(nums))
print(solution_heap(nums))
assert solution(nums)==0

nums = [1,5,0,10,14]
print(solution(nums))
print(solution_iter(nums))
print(solution_minmaxvals(nums))
print(solution_heap(nums))
assert solution(nums)==1

nums = [3,100,20]
print(solution(nums))
print(solution_iter(nums))
print(solution_minmaxvals(nums))
print(solution_heap(nums))
assert solution(nums)==0
