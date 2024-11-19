"""
LC 074: Search a 2D Matrix

You are given an m x n integer matrix `matrix` with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104
"""
# 18 - 33

def search_matrix(matrix, target):
    row = find_row(matrix, target)
    if not row: return False
    i = find_target(row, target)
    return i!=-1

def find_row(matrix, target):
    start = 0
    stop = len(matrix)
    while stop-start > 0:
        m = (start+stop)//2
        if target < matrix[m][0]:
            stop = m
        elif target>matrix[m][-1]:
            start = m + 1
        else:
            return matrix[m]

def find_target(row, target):
    start = 0
    stop = len(row)
    while stop-start>0:
        m = (start+stop)//2
        if target < row[m]:
            stop = m
        elif target > row[m]:
            start = m+1
        else:
            return m
    return -1

def search_matrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    # find row
    start = 0
    stop = m
    row = None 
    while start < stop:
        mid = (start + stop)//2
        if matrix[mid][0] <= target and target <= matrix[mid][n-1]: 
            row = matrix[mid]
            break
        if matrix[mid][n-1] < target:
            start = mid+1
        if matrix[mid][0] > target:
            stop = mid
    if row is None:
        return False

    start = 0
    stop = n

    while start < stop:
        mid = (start + stop)//2
        if row[mid]==rarget:
            return True 
        if row[mid] < target:
            start = mid+1
        if row[mid] > target:
            stop = mid
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(search_matrix(matrix, target))
# Output: true

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(search_matrix(matrix, target))
# Output: false
