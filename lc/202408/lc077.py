"""
LC 077: Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.



Constraints:

    1 <= n <= 20
    1 <= k <= n

"""
def combinations(n, k):
    combo = []
    res = []
    def proc(i):
        if len(combo)==k:
            res.append(list(combo))
            return
        for j in range(i+1, n+1):
            combo.append(j)
            proc(j)
            combo.pop()
    for i in range(1, n+2-k):
        combo.append(i)
        proc(i)
        combo.pop()
    return res

def combinations(n, K):
    combo = []
    res = []
    bt = 0
    for i in range(1, n+2-K):
        stack = [i]
        while stack:
            j = stack.pop()
            if j==bt:
                combo.pop()
                continue
            combo.append(j)
            stack.append(bt)
            if len(combo)==K:
                res.append(combo[:])
                continue
            for k in range(j+1, n+1):
                stack.append(k)
    return res

def combinations(n, k):
    combo = [0] * k
    res = []
    def proc(i, idx):
        if idx==k:
            res.append(list(combo))
            return
        for j in range(i+1, n+1):
            combo[idx] = j
            proc(j, idx+1)
    for i in range(1, n+2-k):
        combo[0] = i
        proc(i, 1)
    return res

def combinations(n, k):
    combo = [0] * k
    res = []
    def proc(i, idx):
        if idx==k:
            res.append(list(combo))
            return
        for j in range(i+1, n+2-(k-idx)):
            combo[idx] = j
            proc(j, idx+1)
    for i in range(1, n+2-k):
        combo[0] = i
        proc(i, 1)
    return res

def combinations(n, k):
    res = []
    combo = [0] * k
    for start_index in range(1, n+2-k):
        stack = [(0, start_index)]
        while stack:
            pos, i = stack.pop()
            combo[pos] = i
            if pos==k-1:
                res.append(combo[:])
                continue
            for j in range(i+1, n+2-(k-pos-1)):
                stack.append((pos+1, j))
    return res

# Interesting algorithm (very efficient)
def combine(n, k):
    if k==1: return [[i] for i in range(1, n+1)]
    combo = [i in range(1, k+1)]
    res = [list(combo)]

    # loop until the first item in the combo is shifted to its max value
    while combo[0] <= n-k:

        # increment last item to n and at each iteration, record combo.
        while combo[-1] < n:
            combo[-1] += 1
            # record the combo
            res.append(list(combo))

        # pop all maxed positions and break at first non-maxed 
        # (e.g. for n=6, k=4, and combo=[1,2,5,6], 3rd and 4th items are maxed.)
        # [1,2,5,6] -> [1,2,5] -> [1,2]
        for j in range(k):
            if combo[-j-1] < n-j:   # if current last combo item is not maxed
                break               # break
            combo.pop()             # otherwise, pop it.

        # increment last (non-maxed) position
        # [1,2] -> [1,3]
        combo[-1] += 1

        # repush the previously popped positions, 
        # each time setting the new position to the value of its predecessor, plus one.
        # [1,3] -> [1,3,4] -> [1,3,4,5]
        while len(combo) < k:
            combo.append(combo[-1] + 1)

        # record the combo
        res.append(list(combo))

    return res


# Same general algorithm, a slightly different approach.
def combinations(n, k):
    if k==n: return [[i for i in range(1, n+1)]]

    combo = [i for i in range(1, k+1)]
    res = [combo[:]]

    pos = k-1 # set pos to increment to the last item in the combo.
    while pos >= 0: # will loop until pos tries to move backward, past the first item in the combo.

        # increment current combo position.
        # e.g. n=8; k=5; combo=[1,3,4,7,8]; pos=2   ->  combo[1,3,5,7,8]
        combo[pos] += 1

        # reset all positions forward of pos 1 value more than their predecessor.
        # e.g. combo[1,2,5,7,8]; pos=2  ->  combo[1,2,5,6,7]
        for j in range(1, k-pos):
            combo[pos+j] = combo[pos+j - 1] + 1

        # record the combo
        res.append(combo[:])

        # if the value at current pos is max for that position move pos down.
        if combo[pos] == n - (k-1 - pos):
            pos -= 1
        # else reset pos back to the last item in the combo.
        else:
            pos = k-1
    return res

def combine(n,k):
    res = []
    # first basic combo 
    combo = [i for i in range(1, k+1)] 
    while True:
        while combo[k-1] <= n:      # loop until maximum value at last position
            res.append(list(combo)) # record combo
            combo[k-1] += 1         # increment last item

        # find first value to increment
        pos = k-1
        local_max = n
        while pos>0 and combo[pos]>local_max:
            pos -= 1
            combo[pos] += 1
            local_max -= 1
        # if first value in combo was incremented past local max (which in this case would be its own maximum), stop.
        if combo[0] > local_max: break

        # set all values forward of first incremented value to one more than their predecessors.
        pos += 1
        while pos < k:
            combo[pos] = combo[pos-1]+1
            pos += 1

    return res

# 1 <= n <= 20
# 1 <= k <= n

print(combinations(1,1))
print(combinations(4,2))
print(combinations(4,3))
print(combinations(4,4))
