"""
LC 073: Set Matrix Zeroes

Given an m x n integer matrix `matrix`, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]



Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1



Follow up:

    A straightforward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?
"""
# 33
def set_zeroes(matrix):
    row_tracker = None
    col_tracker = None
    M = len(matrix)
    N = len(matrix[0])
    for i in range(M):
        for j in range(N):
            if matrix[i][j]==0:
                if row_tracker is None:
                    col_tracker = i
                    row_tracker = j
                matrix[i][row_tracker] = None
                matrix[col_tracker][j] = None
    if row_tracker is None: return
    for i in range(M):
        if i==col_tracker: continue
        if matrix[i][row_tracker] is not None: continue
        for j in range(N):
            if j==row_tracker: continue
            matrix[i][j] = 0
    for j in range(N):
        if j==row_tracker: continue
        if matrix[col_tracker][j] is not None: continue
        for i in range(M):
            if i==col_tracker: continue
            matrix[i][j] = 0
    for row in range(M):
        matrix[row][row_tracker] = 0
    for col in range(N):
        matrix[col_tracker][col] = 0

def set_zeroes(matrix):
    # better approach
    M = len(matrix)
    N = len(matrix[0])
    f_row_zeroes = False
    f_col_zeroes = False
    for i in range(M):
        if matrix[i][0]==0:
            f_col_zeroes = True
    for j in range(N):
        if matrix[0][j]==0:
            f_row_zeroes = True
    for i in range(1, M):
        for j in range(1, N):
            if matrix[i][j]==0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, M):
        if matrix[i][0]==0:
            for j in range(1, N):
                matrix[i][j] = 0
    for j in range(1, N):
        if matrix[0][j]==0:
            for i in range(1, M):
                matrix[i][j] = 0
    if f_row_zeroes:
        for j in range(N):
            matrix[0][j] = 0
    if f_col_zeroes:
        for i in range(M):
            matrix[i][0] = 0


matrix = [[1,1,1],[1,0,1],[1,1,1]]
set_zeroes(matrix)
print(matrix)
# Output: [[1,0,1],[0,0,0],[1,0,1]]

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_zeroes(matrix)
print(matrix)
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
set_zeroes(matrix)
print(matrix)
# Output: [[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
