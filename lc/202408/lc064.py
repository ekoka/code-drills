"""
LC 064: Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 200

"""
def minsum(grid):
    R = len(grid)
    C = len(grid[0])
    paths = [([0] * C) for _ in range(R)] 
    paths[0][0] = grid[0][0]
    inf = float('inf')
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if r==0 and c==0: continue
            top = paths[r-1][c] if r > 0 else inf
            left = paths[r][c-1] if c > 0 else inf
            paths[r][c] = grid[r][c] + min(left, top)
    return paths[-1][-1]

# Better
def minsum(grid):
    rows = len(grid)+1
    cols = len(grid[0])+1
    dp = [[float('inf')] * (cols) for _ in range(rows)]
    dp[0][1] = 0
    dp[1][0] = 0
    for r in range(1, rows):
        for c in range(1, cols):
            dp[r][c] = grid[r-1][c-1] + (dp[r-1][c] if dp[r-1][c] < dp[r][c-1] else dp[r][c-1])
    return dp[-1][-1]

# Best
def minsum(grid):
    rows = len(grid)+1
    cols = len(grid[0])+1
    pre = [float('inf')] * cols
    cur = [float('inf')] * cols
    pre[1] = 0
    for r in range(1, rows):
        for c in range(1, cols):
            cur[c] = grid[r-1][c-1] + (pre[c] if pre[c] < cur[c-1] else cur[c-1])
        pre = cur
    return pre[-1]
