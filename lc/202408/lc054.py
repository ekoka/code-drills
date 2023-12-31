"""
LC 054: Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

    1 → 2 → 3
            ↓
    4 → 5   6
    ↑       ↓
    7 ← 8 ← 9

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

    1 → 2 → 3 → 4
                ↓
  5 → 6 → 7     8
  ↑             ↓
  9 ← 10 ← 11 ← 12

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""
# > 1 h
def spiral_matrix_1(matrix):
    # Better runtime
    bounds = {'l': 0, 'r': len(matrix[0]), 't': 0, 'b':len(matrix)}
    next_direction = {"r":'d', "d":'l', "l":'u', "u":'r'}
    d  = 'r'
    rv = []
    while bounds['l'] < bounds['r'] and bounds['t'] < bounds['b']:
        if d=="r":
            for i in range(bounds['l'], bounds['r']):
                rv.append(matrix[bounds['t']][i])
            bounds['t'] += 1
        elif d=="d":
            for j in range(bounds['t'], bounds['b']):
                rv.append(matrix[j][bounds['r']-1])
            bounds['r'] -= 1
        elif d=="l":
            for i in range(bounds['r']-1, bounds['l']-1, -1):
                rv.append(matrix[bounds['b']-1][i])
            bounds['b'] -= 1
        elif d=="u":
            for j in range(bounds['b']-1, bounds['t']-1, -1):
                rv.append(matrix[j][bounds['l']])
            bounds['l'] += 1
        d = next_direction[d]
    return rv

def spiral_matrix_2(matrix):
    # Better memory
    left, top, right, bottom = 0, 0, len(matrix[0]), len(matrix)
    next_direction = {"right":"down", "down":"left", "left":"up", "up":"right"}
    d  = "right"
    rv = []
    while left < right and top < bottom:
        if d=="right":
            for i in range(left, right):
                rv.append(matrix[top][i])
            top += 1
        elif d=="down":
            for j in range(top, bottom):
                rv.append(matrix[j][right-1])
            right -= 1
        elif d=="left":
            for i in range(right-1, left-1, -1):
                rv.append(matrix[bottom-1][i])
            bottom -= 1
        elif d=="up":
            for j in range(bottom-1, top-1, -1):
                rv.append(matrix[j][left])
            left += 1
        d = next_direction[d]
    return rv

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_matrix_1(matrix))
print(spiral_matrix_2(matrix))
# Output: [1,2,3,6,9,8,7,4,5]

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiral_matrix_1(matrix))
print(spiral_matrix_2(matrix))
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
