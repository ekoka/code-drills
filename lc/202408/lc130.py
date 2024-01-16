"""
LC 130: Surrounding Regions

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

- Connect: A cell is connected to adjacent cells horizontally or vertically.
- Region: To form a region connect every 'O' cell.
- Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.

A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'.
"""
# 22 -

"""
The algorithm:

capture_regions(board) {
    for row, col in border_cells(board) {
        if board[row][col]=="O" {
            mark_protected_region(board, row, col)
        }
    }
    for row, col in all_cells(board) {
        // capture all except protected
        if board[row][col]=="p" {
            board[row][col] = "O"
        } else {
            board[row][col] = "X"
        }
    }
}

border_cells(board) {
    rv = []
    rows, cols = board_sizes(board)
    top, bottom, left, right = 0, rows-1, 0, cols-1
    for c in 0..cols {
        rv.push([top, c])       // top row
        rv.push([bottom, c])    // bottom row
    }
    for r in 0..rows {
        rv.push([r, left])      // left col
        rv.push([r, right])     // right col
    }
    return rv
}

all_cells(board) {
    rv = []
    rows, cols = board_sizes(board)
    for r in 0..rows {
        for c in 0..cols {
            rv.push([r, c])
        }
    }
    return rv
}

mark_protected_region(board, row, col){
    board[row][col] = "p"
    for r,c in non_visited_neighbors(board, row, col) {
        mark_protected_region(board, r, c)
    }
}

non_visited_neighbors(board, row, col) {
    rv = []
    rows, cols = board_sizes(board)
    for r,c in neighboring_cells(row, col) {
        if r>=0 and c>=0 and r<rows and c<cols and board[r][c]=="O":
            rv.append([r,c])
    }
    return rv
}

board_sizes(board) {
    return [size(board), size(board[0])]
}

neighboring_cells(row, col) {
    return [[row,col-1], [row,col+1], [row+1,col], [row-1,col]]
}
"""
def capture(board):
    m = len(board)
    n = len(board[0])
    def border():
        for i in range(m):
            yield (i, 0)
            yield (i, n-1)
        for j in range(n):
            yield (0, j)
            yield (m-1, j)
    for r,c in border():
        if board[r][c]=="o" or board[r][c]=="X": continue
        stack = [(r,c)]
        while stack:
            row, col = stack.pop()
            if board[row][col]=="o": continue
            board[row][col] = "o"
            for r,c in ((row,col+1), (row,col-1), (row+1,col), (row-1,col)):
                if r<0 or r>=m or c<0 or c>=n or board[r][c]=="X" or board[r][c]=="o": continue
                stack.append((r,c))
    for r in range(m):
        for c in range(n):
            if board[r][c]=="o":
                board[r][c] = "O"
            else:
                board[r][c] = "X"

def capture(board):
    m = len(board)
    n = len(board[0])
    def dfs(r,c):
        if r<0 or r>=m or c<0 or c>=n or board[r][c]=="X" or board[r][c]=="o": return
        board[r][c] = "o"
        for x,y in ((0,1), (0,-1), (1,0), (-1,0)):
            dfs(x+r, y+c)
    for i in range(m):
        dfs(i, 0)
        dfs(i, n-1)
    for j in range(n):
        dfs(0, j)
        dfs(m-1, j)
    for r in range(m):
        for c in range(n):
            if board[r][c]=="o":
                board[r][c] = "O"
            else:
                board[r][c] = "X"

def capture(board): # very efficient in both space and time
    m = len(board)
    n = len(board[0])
    def dfs(r,c):
        stack = [(r,c)]
        board[r][c] = "o" # minuscule
        while stack:
            r,c = stack.pop()
            for nr, nc in ((r-1,c), (r, c-1), (r, c+1), (r+1, c)):
                if nr < 0 or nr >= m or nc < 0 or nc >= n or board[nr][nc] != "O": continue
                board[nr][nc] = "o"
                stack.append((nr, nc))
    for c in range(n):
        if board[0][c]=="O": 
            dfs(0, c)
        if board[m-1][c]=="O":
            dfs(m-1, c)
    for r in range(m):
        if board[r][0]=="O":
            dfs(r, 0)
        if board[r][n-1]=="O":
            dfs(r, n-1)
    for r in range(m):
        for c in range(n):
            if board[r][c]=="o":
                board[r][c] = "O"
            else:
                board[r][c] = "X"

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
capture(board)
print(board)
#Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]


board = [["X"]]
capture(board)
print(board)
# Output: [["X"]]
