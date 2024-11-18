"""
LC 079: Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false



Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
# 04 -
def search(board, word):
    N = len(word)
    m = len(board)
    n = len(board[0])
    col = lambda: [False] * n
    visited = [col() for _ in range(m)]
    def bt(r, c, match):
        if board[r][c]!=word[match]:
            return False
        match += 1
        if match==N:
            return True
        visited[r][c] = True
        for i,j in neighbors(r,c,m,n,visited):
            if bt(i,j, match):
                return True
        visited[r][c] = False
        return False
    for row in range(m):
        for col in range(n):
            if bt(row, col, 0):
                return True
    return False


def search(board, word):
    rowcnt, colcnt, charcnt = len(board), len(board[0]), len(word)
    mkrow = lambda: [False] * colcnt
    vis = [mkrow() for _ in range(rowcnt)]

    def neighbors(r,c):
        rv = []
        for x,y in (r,c-1), (r,c+1), (r-1,c), (r+1,c):
            if (x < 0 or y < 0
                or x==rowcnt or y==colcnt
                or vis[x][y]): continue
            rv.append((x,y))
        return rv

    def bt(r, c, i):
        if board[r][c]!=word[i]: return False
        if i==charcnt-1: return True
        i += 1
        vis[r][c] = True
        for x,y in neighbors(r,c):
            if bt(x,y,i): return True
        vis[r][c] = False
        return False

    for r in range(rowcnt):
        for c in range(colcnt):
            if bt(r, c, 0): return True
    return False

def search(board, word):
    # not as fast as expected
    rowcnt, colcnt, charcnt, visited = len(board), len(board[0]), len(word), '.'
    def neighbors(r,c):
        rv = []
        for x,y in (r,c-1), (r,c+1), (r-1,c), (r+1,c):
            if (x < 0 or y < 0
                or x==rowcnt or y==colcnt
                or board[x][y]==visited): continue
            rv.append((x,y))
        return rv

    def bt(r, c, i):
        if board[r][c]!=word[i]: return False
        if i==charcnt-1: return True
        char = board[r][c]
        board[r][c] = visited
        i += 1
        for x,y in neighbors(r,c):
            if bt(x,y,i): return True
        board[r][c] = char
        return False

    for r in range(rowcnt):
        for c in range(colcnt):
            if bt(r, c, 0): return True
    return False

def word_search(board, word):
    m = len(board)
    n = len(board[0])
    visited = [ [False] * (n+1) for _ in range(m+1) ]
    def bt(r, c, i):
        visited[r][c] = True
        if i==len(word): return True
        if board[r][c]!=word[i]: return False
        nxt_i = i+1
        for nxt_r, nxt_c in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
            if nxt_r >= 0 and nxt_c >= 0 and nxt_r <= m and nxt_c <= n and not visited[nxt_r][nxt_c]:
                if bt(nxt_r, nxt_c, nxt_i): return True
                visited[nxt_r][nxt_c] = False
        return False
    for row in range(m):
        for col in range(n):
            if board[row][col]!=word[0]: continue
            if bt(row, col, 0): return True
            visited[row][col] = False
    return False

# using sets, but less efficient
def word_search(board, word):
    m = len(board)
    n = len(board[0])
    if m*n < len(word): return False
    # backtracking routine
    visited = set()
    def bt(r, c, i):
        if board[r][c]!=word[i]: return False
        i += 1
        if i==len(word): return True
        for nxt_r, nxt_c in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
            if nxt_r >= 0 and nxt_c >= 0 and nxt_r < m and nxt_c < n and (next_r, next_c) not in visited:
                visited.add((r,c))
                if bt(nxt_r, nxt_c, i): return True
                visited.remove((r,c))
        return False
    for row in range(m):
        for col in range(n):
            if board[row][col]!=word[0]: continue
            visited.add((row,col))
            if bt(row, col, 0): return True
            visited.remove((row,col))
    return False

def word_search(board, word):
    m = len(board)
    n = len(board[0])
    W = len(word)
    
    first_char = word[0]
    last_char = word[-1]
    char_count = {first_char:0, last_char:0}
    char_indexes = {first_char:[], last_char:[]}
    for r in range(m):
        for c in range(n):
            if board[r][c]==first_char:
                char_count[first_char] += 1
                char_indexes[first_char].append((r,c))
            elif board[r][c]==last_char:
                char_count[last_char] += 1
                char_indexes[last_char].append((r,c))

    if char_count[first_char] > char_count[last_char]:
        word = word[::-1]
        board_indexes = char_indexes[last_char]
    else:
        board_indexes = char_indexes[first_char]


    def neighbors(r,c):
        if (r,c) in neighbors.memo:
            return neighbors.memo[(r,c)]
        memo = neighbors.memo[(r,c)] = []
        for nxt_r, nxt_c in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if nxt_r < 0 or nxt_r >= m or nxt_c < 0 or nxt_c >= n: continue
            memo.append((nxt_r, nxt_c))
        return memo
    neighbors.memo = {}


    def bt(r,c,i):
        if i+1==W: return True
        nxt_i = i+1        
        for nxt_r, nxt_c in neighbors(r,c):
            char = board[nxt_r][nxt_c]
            if char!=word[nxt_i]: continue
            board[nxt_r][nxt_c] = '#'
            if bt(nxt_r, nxt_c, nxt_i):
                return True
            board[nxt_r][nxt_c] = char
    for r,c in board_indexes:
        char = board[r][c]
        board[r][c] = '#'
        if bt(r,c,0): 
            return True
        board[r][c] = char
    return False


def word_search(board, word):
    m = len(board)
    n = len(board[0])
    W = len(word)
    
    first_char = word[0]
    last_char = word[-1]
    char_count = {first_char:0, last_char:0}
    char_indexes = {first_char:[], last_char:[]}
    for r in range(m):
        for c in range(n):
            if board[r][c]==first_char:
                char_count[first_char] += 1
                char_indexes[first_char].append((r,c))
            elif board[r][c]==last_char:
                char_count[last_char] += 1
                char_indexes[last_char].append((r,c))

    if char_count[first_char] > char_count[last_char]:
        word = word[::-1]
        board_indexes = char_indexes[last_char]
    else:
        board_indexes = char_indexes[first_char]


    def neighbors(r,c):
        if (r,c) in neighbors.memo:
            return neighbors.memo[(r,c)]
        memo = neighbors.memo[(r,c)] = []
        for nxt_r, nxt_c in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if nxt_r < 0 or nxt_r >= m or nxt_c < 0 or nxt_c >= n: continue
            memo.append((nxt_r, nxt_c))
        return memo
    neighbors.memo = {}


    def bt(r,c,i):
        if i+1==W: return True
        nxt_i = i+1        
        for nxt_r, nxt_c in neighbors(r,c):
            char = board[nxt_r][nxt_c]
            if char!=word[nxt_i]: continue
            board[nxt_r][nxt_c] = '#'
            if bt(nxt_r, nxt_c, nxt_i):
                return True
            board[nxt_r][nxt_c] = char
    for r,c in board_indexes:
        char = board[r][c]
        board[r][c] = '#'
        if bt(r,c,0): 
            return True
        board[r][c] = char
    return False

# iterative
def word_search(board, word):
    m = len(board)
    n = len(board[0])
    W = len(word)
    
    first_char = word[0]
    last_char = word[-1]
    char_count = {first_char:0, last_char:0}
    char_indexes = {first_char:[], last_char:[]}
    for r in range(m):
        for c in range(n):
            if board[r][c]==first_char:
                char_count[first_char] += 1
                char_indexes[first_char].append((r,c))
            elif board[r][c]==last_char:
                char_count[last_char] += 1
                char_indexes[last_char].append((r,c))

    if char_count[first_char] > char_count[last_char]:
        word = word[::-1]
        board_indexes = char_indexes[last_char]
    else:
        board_indexes = char_indexes[first_char]


    def neighbors(r,c):
        if (r,c) in neighbors.memo:
            return neighbors.memo[(r,c)]
        memo = neighbors.memo[(r,c)] = []
        for nxt_r, nxt_c in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if nxt_r < 0 or nxt_r >= m or nxt_c < 0 or nxt_c >= n: continue
            memo.append((nxt_r, nxt_c))
        return memo
    neighbors.memo = {}

    bt = -1
    visited = set()
    for r,c in board_indexes:
        stack = [(r,c,0)]
        while stack:
            r,c,i = stack.pop() 
            if i==bt:
                visited.remove((r,c))
                continue

            stack.append((r,c,bt))
            visited.add((r,c))

            if i+1==W: return True

            for nxt_r, nxt_c in neighbors(r,c):
                if board[nxt_r][nxt_c]!=word[i+1]: continue
                if (nxt_r, nxt_c) in visited: continue
                stack.append((nxt_r, nxt_c, i+1))
    return False

"""
## Optimization opportunities

1. does the size of the board even matches the word's?

    if m*n < len(word): return False

2. does each character in the word occur at least as many times in the board?

    board_chars = {}
    for row in range(m):
        for col in range(n):
            char = board[row][col]
            board_chars[char] = board_chars.get(char, 0) + 1

    word_chars = {}
    for char in word:
        word_chars[char] = word_chars.get(char, 0) + 1
        
    for char, count in word_chars.items():
        if count > board_chars.get(char, 0):
            return False

3. we can also choose to traverse the word in reverse, giving us the opportunity to start the traversal from whichever of the first or last character occurs the least on the board.

    if board_chars[word[0]] > board_chars[word[-1]]:
        word = "".join(reversed(word))

    for row in range(m):
        for col in range(n):
            visited.add((row, col))
            if bt(row, col, 0): return True
            visited.remove((row, col))

"""

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"
print(search(board, word))
# Output: true

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "SEE"
print(search(board, word))
# Output: true

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCB"
print(search(board, word))
# Output: false

board = [["a"]]
word = "a"
print(search(board, word))
