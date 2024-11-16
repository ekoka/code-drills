"""
LC 046: Permutations
Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]



Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
"""
# 22 - 30
def permutations(nums):
    rv = []
    combo = []
    skip = set()
    def bt():
        rec = len(combo)==len(nums)-1
        for n in nums:
            if n in skip: continue
            combo.append(n)
            skip.add(n)
            if rec:
                rv.append(list(combo))
            else:
                bt()
            combo.pop()
            skip.remove(n)
    bt()
    return rv

def permutations(nums):
    N = len(nums)
    rv = []
    combo = []
    def bt(remaining):
        rec = len(combo)==N-1
        for n in list(remaining):
            combo.append(n)
            if rec:
                rv.append(list(combo))
            else:
                bt(remaining - {n})
            combo.pop()
    bt(set(nums))
    return rv

# iterative
def permutations(nums):
    res = []
    for start in range(len(nums)):
        stack = [(start, False)]
        visited = set()
        combo = []
        while stack:
            i, pop = stack.pop()
            if pop:
                combo.pop()
                visited.remove(i)
            else:
                stack.append((i, True))
                combo.append(nums[i])
                visited.add(i)
                if len(combo)==len(nums):
                    res.append(list(combo))
                    continue
                for j in range(len(nums)):
                    if j in visited: continue
                    stack.append((j, False))
    return res

# same, but simpler
def permutations(nums):
    res = []
    for start in nums:
        stack = [(start, False)]
        combo = []
        while stack:
            n, pop = stack.pop()
            if pop:
                combo.pop()
            else:
                stack.append((None, True))
                combo.append(n)
                if len(combo)==len(nums):
                    res.append(list(combo))
                    continue
                for nxt_n in nums:
                    if nxt_n in combo: continue
                    stack.append((nxt_n, False))
    return res

def permutations(nums):
    res = []
    combo = []  # combo is small enough (N=6) that we can use it directly as a set.
    bt = -12    # out of bound value used to mark backtracking step
    for n in nums: 
        stack = [n]
        while stack:
            n = stack.pop()
            if n == bt:
                combo.pop()
                continue
            combo.append(n)
            stack.append(bt)
            if len(combo)==len(nums):
                res.append(list(combo))
                continue
            for m in nums:
                if m in combo: continue
                stack.append(m)
    return res

def permutations(nums):
    n = len(nums)
    res = []
    combo = []
    def proc():
        if len(combo)==n:
            res.append(combo[:])
            return
        for j in nums:
            if j in combo: continue
            combo.append(j)
            proc()
            combo.pop()
    proc()
    return res

def permutations(nums):
    n = len(nums)
    bt = 11
    combo = []
    res = []
    for starting_num in nums:
        stack = [starting_num]
        while stack:
            num = stack.pop()
            if num==bt:
                combo.pop()
                continue
            combo.append(num)
            stack.append(bt)
            if len(combo)==n:
                res.append(combo[:])
                continue
            for j in nums:
                if j in combo: continue
                stack.append(j)
    return res

nums = [1,2,3]
print(permutations(nums))
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

nums = [0,1]
print(permutations(nums))
#Output: [[0,1],[1,0]]

nums = [1]
print(permutations(nums))
#Output: [[1]]
