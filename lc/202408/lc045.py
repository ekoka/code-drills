"""
LC 045 : Jump Game II

You are given a 0-indexed array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at `nums[i]`, you can jump to any `nums[i + j]` where:

    0 <= j <= nums[i] and
    i + j < n

Return the minimum number of jumps to reach `nums[n - 1]`. The test cases are generated such that you can reach `nums[n - 1]`.

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2



Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 1000
    It's guaranteed that you can reach nums[n - 1].

"""
#24
def minjump(nums):
    last = len(nums) - 1
    offset = [0]
    jumps = [0]
    result = float('inf')
    while offset:
        o = offset.pop()
        j = jumps.pop() + 1
        for steps in range(nums[o]):
            if steps + o + 1 >= last:
                result = min(j, result)
                continue
            offset.append(steps + o + 1)
            jumps.append(j)
    return result

def minjump(nums):
    last = len(nums) - 1
    offset = [0]
    jumps = [0]
    rv = float('inf')
    while offset:
        next_offset = []
        next_jumps = []
        for i in range(len(offset)):
            o = offset[i]
            j = jumps[i] + 1
            for steps in range(nums[o]):
                if steps + o + 1 >= last:
                    rv = min(j, rv)
                    continue
                next_offset.append(steps + o + 1)
                next_jumps.append(j)
        offset = next_offset
        jumps = next_jumps
    return rv


def minjump(nums):
    end = len(nums) - 1
    def helper(offset, jumps):
        rv = float('inf')
        for steps in range(nums[offset]):
            if steps + offset + 1 >= end:
                return jumps + 1
            rv = min(rv, helper(steps+offset+1, jumps+1))
        return rv
    return helper(0, 0)

def minjump(nums):
    N = len(nums)
    rv = [-1] * N
    rv[N-1] = 0
    for i in range(N-2, -1, -1):
        j = i+nums[i]
        if j >= N-1:
            rv[i] = 1
        else:
            m = -1
            for k in range(i,j+1):
                if rv[k]==-1: continue
                if m==-1 or rv[k] < m:
                    m = rv[k]
            rv[i] = -1 if m==-1 else m+1
    return rv[0]

def minjump(nums):
    N = len(nums)
    if N==1: return 0
    stack = [0]
    k = 0
    cnt = 1
    while stack:
        new_stack = []
        while stack:
            i = stack.pop()
            for j in range(k+1, i+nums[i]+1):
                if j==N-1:
                    return cnt
                new_stack.append(j)
                k = j
        stack = new_stack
        cnt += 1
    return -1

def minjump(nums):
    N = len(nums)
    if N==1: return 0
    jump = [0] * N
    k = 0 # latest visited index
    for i in range(N-1):
        for j in range(k+1, i+nums[i]+1):
            if j==N-1: return jump[i]+1
            jump[j] = jump[i]+1
            k = j
    return -1

# BFS

def minjump(nums):
    q = deque([0])
    visited = 0
    jumps = 0
    while q:
        next_q = deque()
        while q:
            i = q.popleft()
            if i >= len(nums)-1: return jumps
            if visited >= i+nums[i]: continue
            for j in range(visited+1, nums[i]+i+1):
                next_q.append(j)
            visited = i+nums[i]
        q = next_q
        jumps += 1

def minjump(nums): # BFS adaptation
    n = len(nums)
    current_range = [0, 1] # range (start & stop) of currently reachable indexes.
    jumps = 0
    # Problem assumes that the end is reachable.
    # Looping until `stop` reaches past the last item.
    while current_range[1] < n:
        next_range = [current_range[1], current_range[1]] # next level in BFS
        for i in range(current_range[0], current_range[1]):
            next_range[1] = max(next_range[1], i+nums[i]+1)
        current_range = next_range
        jumps += 1
    return jumps


def minjump(nums): # BFS adaptation
    n = len(nums)
    start, stop = 0, 1 # range of currently reachable indexes.
    jumps = 0
    # Problem assumes that the end is reachable.
    # Looping until `stop` reaches past the last item.
    while stop < n:
        next_stop = stop # stop for next level in BFS
        for i in range(start, stop):
            next_stop = max(next_stop, i+nums[i]+1)
        start = stop 
        stop = next_stop
        jumps += 1  # up one level 
    return jumps

print(minjump([2,3,1,1,4]))
# 2
print(minjump([2,3,0,1,4]))
# 2
print(minjump([3,2,1,0,4]))
# -1 or inf
