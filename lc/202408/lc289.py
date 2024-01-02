"""
LC 289: Game of Life

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an `m x n` grid of cells, where each cell has an initial state: *live* (represented by a 1) or *dead* (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Example 1:

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 25
    board[i][j] is 0 or 1.

Follow up:

- Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
- In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""
def life(board):
    m = len(board)
    n = len(board[0])
    cells = [(r,c) for r in range(m) for c in range(n)]
    for r,c in cells:
        neighbors = 0
        for x,y in ((r-1,c-1), (r-1,c), (r-1,c+1), (r,c-1), (r,c+1), (r+1,c-1), (r+1,c), (r+1,c+1)):
            #if not all((x>=0, x<m, y>=0, y<n)): continue # slower than the more explicit boolean form below
            if not (x>=0 and x<m and y>=0 and y<n): continue
            if board[x][y]==1 or board[x][y]==2:
                neighbors += 1
        if board[r][c]==1:
            if neighbors < 2:
                board[r][c] = 2
            elif neighbors > 3:
                board[r][c] = 2 # currently live and about to die
        else:
            if neighbors==3:
                board[r][c] = 3 # currently dead and about to live
    for r,c in cells:
        if board[r][c]==2:      # currently live and about to die
            board[r][c] = 0
        elif board[r][c]==3:    # currently dead and about to live
            board[r][c] = 1

# not as efficient because of syntax sugar (generator, lambda, all(), sum())
def life(board):
    m = len(board)
    n = len(board[0])
    cells = lambda: ((r,c) for r in range(m) for c in range(n))
    for r,c in cells():
        neighbors = ((r-1,c-1), (r-1,c), (r-1,c+1), (r,c-1), (r,c+1), (r+1, c-1), (r+1, c), (r+1, c+1))
        live_neighbors = sum(1 for x, y in neighbors if all((x>=0, x<m, y>=0, y<n)) and board[x][y] > 0)
        if board[r][c]==1:
            if live_neighbors < 2 or live_neighbors > 3:
                board[r][c] = 2     # currently alive, about to be killed
        else: # board[r][c]==0
            if live_neighbors==3:
                board[r][c] = -1    # currently dead, about to be resurrected
    for r,c in cells():
        if board[r][c]==2:
            board[r][c] = 0
        elif board[r][c]==-1:
            board[r][c] = 1


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
life(board)
print(board)
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

board = [[1,1],[1,0]]
life(board)
print(board)
# Output: [[1,1],[1,1]]
