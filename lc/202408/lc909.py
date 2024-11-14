"""
LC 909: Snakes and Ladders

You are given an n x n integer matrix `board` where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. `board[n - 1][0]`) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square `curr`, do the following:

- Choose a destination square `next` with a label in the range `[curr + 1, min(curr + 6, n2)]`.
    - This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.

- If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.

- The game ends when you reach the square n2.

A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

- For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.

Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.

Example 1:

Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation:
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.

Example 2:

Input: board = [[-1,-1],[-1,3]]
Output: 1



Constraints:

    n == board.length == board[i].length
    2 <= n <= 20
    board[i][j] is either -1 or in the range [1, n2].
    The squares labeled 1 and n2 are not the starting points of any snake or ladder.

"""
# 14
def label_to_coords(label, N):
    r = (label-1)//N
    c = (label-1)%N
    if r%2:
        c = N-c-1
    return N-r-1, c


from collections import deque
def minmoves(board):
    N = len(board)
    max_label = N*N
    def next_labels(l):
        return [i for i in range(l+1, l+7) if i <= max_label]
    solution = [float('inf')] * (max_label + 1)
    solution[1] = 0
    q = deque([1])
    while q:
        label = q.popleft()
        steps = solution[label]
        if steps >= solution[max_label]: continue
        for l in next_labels(label):
            r,c = label_to_coords(l, N)
            if board[r][c]!=-1:
                l = board[r][c]
            if solution[l] <= steps+1: continue
            solution[l] = steps + 1
            q.append(l)
    return solution[max_label]


def minmoves(board, debug=False):
    N = len(board)
    max_lbl = N*N

    def resolve_label(lbl):
        r = (lbl-1)//N
        c = (lbl-1)%N
        if r%2:
            c = N-c-1
        move = board[N-r-1][c]
        return lbl if move==-1 else move

    steps = [-1] * (max_lbl+1)
    steps[1], q = 0, [1]
    while q:
        next_q = []
        while q:
            lbl = q.pop()
            stp = steps[lbl]
            for i in range(1, 7):
                nxt_lbl = resolve_label(lbl+i)
                if nxt_lbl==max_lbl:
                    return stp+1
                if steps[nxt_lbl]==-1:
                    steps[nxt_lbl] = stp+1
                    next_q.append(nxt_lbl)
        q = next_q
    return -1

def minmoves(board):
    N = len(board)
    positions = []
    step = -1
    for r in range(N-1, -1, -1):
        start, end, step = (0, N, 1) if step==-1 else (N-1, -1, -1)
        for c in range(start, end, step):
            positions.append(board[r][c])
    stack = [0]
    discovered = set()
    rolls = 0
    while stack:
        nxt_stack = []
        rolls += 1
        while stack:
            i = stack.pop()
            if i==len(positions)-1: 
                return rolls-1
            for j in range(i+1, i+7):
                if j >= len(positions): break
                if j in discovered: continue                
                discovered.add(j)
                if positions[j]!=-1:
                    j = positions[j]-1
                nxt_stack.append(j)
        stack = nxt_stack
    return -1

            
board = [
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,35,-1,-1,13,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,15,-1,-1,-1,-1]
]
print(minmoves(board))

board = [[-1,-1],[-1,3]]
print(minmoves(board))

board = [[1,1,-1],
         [1,1,1],
         [-1,1,1]]
print(minmoves(board))

board = [[-1,1,2,-1],
         [2,13,15,-1],
         [-1,10,-1,-1],
         [-1,6,2,8]]
print(minmoves(board))

board = [[-1,-1,-1],
         [-1,9,8],
         [-1,8,9]]
print(minmoves(board, True))
