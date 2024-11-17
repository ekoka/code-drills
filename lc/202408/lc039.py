"""
LC 039 Combination Sum

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of candidates where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []



Constraints:

    1 <= candidates.length <= 30
    2 <= candidates[i] <= 40
    All elements of candidates are distinct.
    1 <= target <= 40
"""
# 56
def combination_sum(candidates, target):
    rv = []
    combo = []
    def bt(start, k):
        for c in candidates:
            if c < start: continue
            v = k+c
            if v==target:
                rv.append(list(combo))
                rv[-1].append(c)
            elif v<target:
                combo.append(c)
                bt(c, v)
                combo.pop()
    bt(0, 0)
    return rv

def combination_sum(candidates, target):
    combo = []
    rv = []
    def bt(i, tgt):
        combo.append(candidates[i])
        tgt -= candidates[i]
        if tgt==0:
            rv.append(list(combo))
        elif tgt > 0:
            for j in range(i, len(candidates)):
                if candidates[j] > tgt: continue
                bt(j, tgt)
        combo.pop()
    for start in range(len(candidates)):
        bt(start, target)
    return rv

def combination_sum(candidates, target):
    rv = []
    combo = [] 
    for start in range(len(candidates)):
        if candidates[start] > target: continue 
        stack = [(start, False)]
        while stack:
            i, visited = stack.pop()
            if visited:
                target += combo.pop()
            else:
                stack.append((i, True))
                target -= candidates[i]
                combo.append(candidates[i])
                if target==0:
                    rv.append(list(combo))
                else:
                    for j in range(i, len(candidates)):
                        if candidates[j] > target: continue
                        stack.append((j, False))
    return rv

def combination_sum(candidates, target):
    res = []
    combo = []
    bt = -1
    for i in range(len(candidates)):
        c = candidates[i]
        if c > target: continue
        stack = [(i, c)]
        while stack:
            i, t = stack.pop()
            if t == bt:
                combo.pop()
                continue

            stack.append((None,bt))
            combo.append(candidates[i])
            if t==target:
                res.append(combo[:])
                continue

            for j in range(i, len(candidates)):
                nxt_t = t+candidates[j]
                if nxt_t > target: continue
                stack.append((j, nxt_t))
    return res

def combination_sum(candidates, target):
    n = len(candidates)
    res = []
    combo = []
    candidates.sort()
    def proc(i, t):
        combo.append(candidates[i])
        t -= candidates[i]
        if t==0:
            res.append(combo[:])
        else:
            for j in range(i, n):
                if t < candidates[j]: continue
                proc(j, t)
        combo.pop()

    for i in range(n):
        if target < candidates[i]: continue
        proc(i, target)
    return res

def combination_sum(candidates, target):
    n = len(candidates)
    bt = n
    res = []
    combo = []
    for starting_index in range(n):
        if candidates[starting_index] > target: continue
        stack = [(starting_index, target)]
        while stack:
            i, t = stack.pop()
            if i==bt:
                combo.pop()
                continue
            t -= candidates[i]
            combo.append(candidates[i])
            stack.append((bt, None))
            if t==0:
                res.append(combo[:])
                continue
            for j in range(i, n):
                if candidates[j] > t: continue
                stack.append((j, t))
    return res

candidates = [2,3,6,7]
target = 7
print(combination_sum(candidates, target))
# Output: [[2,2,3],[7]]

candidates = [2,3,5]
target = 8
print(combination_sum(candidates, target))
# Output: [[2,2,2,2],[2,3,3],[3,5]]

candidates = [2]
target = 1
print(combination_sum(candidates, target))
#Output: []
