"""
LC 200: Number of Islands

Given an m x n 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""
# 12 -

def number_of_islands(gri):
    count = 0
    M = len(grid)
    N = len(grid[0])
    row = lambda : [False] * N
    visited = [row() for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if grid[i][j]=="0" or visited[i][j]: continue
            count += 1
            stack = [(i,j)]
            while stack:
                row, col = stack.pop()
                visited[row][col] = True
                for r,c in ((row+1, col), (row, col+1), (row-1, col), (row, col-1)):
                    if r < 0 or c < 0 or r >= M or c >= N or grid[r][c]=="0" or visited[r][c]:
                        continue
                    stack.append((r,c))
    return count

"""
According to leetcode's analyis, this next version surprisingly doesn't do better than the previous and doesn't even save much more memory .
"""
def number_of_islands(grid):
    count = 0
    M = len(grid)
    N = len(grid[0])
    for i in range(M):
        for j in range(N):
            if grid[i][j]=="0" or grid[i][j]=="-1": continue
            count += 1
            stack = [(i,j)]
            while stack:
                row, col = stack.pop()
                grid[row][col] = "-1"
                for r,c in ((row+1, col), (row, col+1), (row-1, col), (row, col-1)):
                    if r < 0 or c < 0 or r >= M or c >= N or grid[r][c]=="0" or grid[r][c]=="-1":
                        continue
                    stack.append((r,c))
    return count

# most efficient
def number_of_islands(grid):
    m = len(grid)
    n = len(grid[0])
    islands = 0
    for row in range(m):
        for col in range(n):
            if grid[row][col]!="1": continue
            grid[row][col] = "2"
            stack = [(row,col)]
            while stack:
                r, c = stack.pop()
                for i, j in ((r-1, c), (r, c-1), (r, c+1), (r+1, c)):
                    if i < 0 or j < 0 or i >= m or j >= n: continue
                    if grid[i][j]!="1": continue
                    grid[i][j] = "2"
                    stack.append((i,j))
            islands += 1
    return islands

def number_of_islands(grid):
    res = 0
    lands = set()
    m = len(grid)
    n  = len(grid[0])
    for row in range(m):
        for col in range(n):
            if grid[row][col]!="1": continue 
            lands.add((row,col))
    while lands:
        stack = {lands.pop()}
        while stack:
            r, c = stack.pop()
            for i, j in ((r-1, c), (r, c-1), (r, c+1), (r+1, c)):
                if (i,j) not in lands: continue
                lands.remove((i,j))
                stack.add((i,j))
        res += 1
    return res

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(number_of_islands(grid))
# Output: 1

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(number_of_islands(grid))
# Output: 3

grid = [
  ["1","1","1"],
  ["0","1","0"],
  ["1","1","1"],
]
print(number_of_islands(grid))
# Output: 1

grid = [
    ["1","0","1","1","0","1","1"]
]
print(number_of_islands(grid))
# Output: 3

grid = [
    ["0","1","0"],
    ["1","0","1"],
    ["0","1","0"]
]
print(number_of_islands(grid, True))
# Output: 4
