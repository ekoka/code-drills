"""
LC 221: Maximal Square
Given an `m x n` binary `matrix` filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:

Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:

Input: matrix = [["0"]]
Output: 0

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 300
    matrix[i][j] is '0' or '1'.
"""
# 29


def solution1(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    M = [ [ 0 for _ in range(cols+1) ] for _ in range(rows+1) ]
    maxsquare = 0
    for r in range(1, rows+1):
        for c in range(1, cols+1):
            M[r][c] = int(matrix[r-1][c-1])
        maxsquare += sum(M[r])
    if maxsquare==0:
        return 0
    maxsquare = 1
    square = [ [0] * (cols+1) for _ in range(rows+1) ]
    for r in range(1, rows+1):
        for c in range(1, cols+1):
            if square[r-1][c-1]>=1 and square[r-1][c]>=1 and square[r][c-1]>=1 and M[r][c]==1:
                square[r][c] = min(square[r-1][c-1], square[r-1][c], square[r][c-1]) + 1
                maxsquare = max(maxsquare, square[r][c])
            else:
                square[r][c] = M[r][c]
    return maxsquare * maxsquare

def solution2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    prev = [ 0 ] * (cols+1)
    curr = [ 0 ] * (cols+1)
    maxsquare = 0
    singlesquare = 0
    for r in range(1, rows+1):
        for c in range(1, cols+1):
            v = int(matrix[r-1][c-1])
            if v==1 and prev[c-1]>=1 and prev[c]>=1 and curr[c-1]>=1:
                curr[c] = min(prev[c-1], prev[c], curr[c-1]) + 1
                maxsquare = max(maxsquare, curr[c])
            else:
                curr[c] = v 
                singlesquare += v
        prev, curr = curr, prev 
    if maxsquare==0:
        return 1 if singlesquare >= 1 else 0
    return maxsquare * maxsquare

def solution2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    prev = [ 0 ] * (cols+1)
    curr = [ 0 ] * (cols+1)
    maxsquare = 0
    for r in range(1, rows+1):
        for c in range(1, cols+1):
            if matrix[r-1][c-1]=="0": 
                curr[c] = 0
            else:
                curr[c] = 1  + min(prev[c-1], prev[c], curr[c-1])
                maxsquare = max(maxsquare, curr[c])
        prev, curr = curr, prev 
    return maxsquare * maxsquare

def solution(matrix):
    rows = len(matrix) +1
    cols = len(matrix[0])+1
    prev = [ 0 ] * (cols)
    curr = [ 0 ] * (cols)
    maxsquare = 0
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r-1][c-1]=="0":
                curr[c] = 0
            else:
                #curr[c] = 1  + min(prev[c-1], prev[c], curr[c-1])
                v = prev[c] if prev[c-1] > prev[c] else prev[c-1]
                if v > curr[c-1]:
                    v = curr[c-1]
                curr[c] = 1  + v
                if curr[c] > maxsquare:
                   maxsquare = curr[c]
        prev, curr = curr, prev
    return maxsquare * maxsquare

def maxsquare(matrix):
    m = len(matrix)
    n = len(matrix[0])
    memo = [ [0] * (n+1) for _ in range(m+1) ]
    res = 0
    def min(x, y, z):
        if x < y and x < z:
            return x
        if y < z:
            return y
        return z
    for i in range(1, m+1):
        for j in range(1, n+1):
            v = 1 if matrix[i-1][j-1]=="1" else 0
            pre = min(memo[i-1][j], memo[i][j-1], memo[i-1][j-1])
            memo[i][j] = pre + v 
            if res < memo[i][j]:
                res = memo[i][j]
    return res*res

def maxsquare(matrix):
    m = len(matrix)+1
    n = len(matrix[0])+1
    memo = [ [0] * n for _ in range(m) ]
    res = 0
    def min(x, y, z):
        if x < y and x < z:
            return x
        if y < z:
            return y
        return z
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i-1][j-1]=="0": continue
            memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1], memo[i-1][j-1])
            if res < memo[i][j]:
                res = memo[i][j]
    return res*res

def maxsquare(matrix):
    m = len(matrix)+1
    n = len(matrix[0])+1
    pre = [0] * n 
    cur = [0] * n
    res = 0
    def min(x, y, z):
        if x < y and x < z:
            return x
        if y < z:
            return y
        return z
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i-1][j-1]=="0": 
                cur[j] = 0
                continue
            cur[j] = 1 + min(pre[j], cur[j-1], pre[j-1])
            if res < cur[j]:
                res = cur[j]
        pre, cur = cur, pre
    return res*res

def maxsquare(matrix):
    m = len(matrix)+1
    n = len(matrix[0])+1
    cur = [0] * n
    res = 0
    def min(x, y, z):
        if x < y and x < z:
            return x
        if y < z:
            return y
        return z
    for i in range(1, m):
        pre = 0 # normally pre[i-1], but we got rid of the previous row
        for j in range(1, n):
            next_pre = cur[j]
            if matrix[i-1][j-1]=="0": 
                cur[j] = 0
                pre = next_pre
                continue
            cur[j] = 1 + min(cur[j], cur[j-1], prepre)
            pre = next_pre
            if res < cur[j]:
                res = cur[j]
    return res*res


def maxsquare(matrix):
    m = len(matrix)+1
    n = len(matrix[0])+1
    memo = [0] * n
    res = 0
    def min(x, y, z):
        if x < y and x < z:
            return x
        if y < z:
            return y
        return z
    for i in range(1, m):
        pre = 0
        for j in range(1, n):
            if matrix[i-1][j-1]=="0": 
                memo[j], pre = 0, memo[j]
                continue
            memo[j], pre = (1 + min(memo[j], memo[j-1], pre), memo[j])
            if res < memo[j]:
                res = memo[j]
    return res*res
