"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]



Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000

"""
# 32 -
def rotate(matrix):
    N = len(matrix)
    for j in range(N//2):           # for layer
        for i in range(j, N-j-1):   # for index in layer
            row, col = j, i
            val = matrix[row][col]
            for _ in range(4):
                row, col = col, N-row-1
                tmp = matrix[row][col]
                matrix[row][col] = val
                val = tmp

def rotate(matrix):
    N = len(matrix)
    for row in range(N//2): # for each outer layer
        for col in range(row, N-row-1): # for each cell in the top row
            # mapping: next_coord(row, col) => (col, N-row-1)
            top = M[row][col]
            right = M[col][N-row-1]
            bottom = M[N-row-1][N-col-1]
            #left = M[N-col-1][N-(N-row-1)-1]
            left = M[N-col-1][row]

            M[row][col] = left
            M[col][N-row-1] = top
            M[N-row-1][N-col-1] = right
            #M[N-col-1][N-(N-row-1)-1] = bottom
            M[N-col-1][row] = bottom

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)
# Output: [[7,4,1],[8,5,2],[9,6,3]]

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix)
print(matrix)
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
