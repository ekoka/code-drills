# 01 - 36
"""
LC 212 : Word Search II

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= words.length <= 3 * 104
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    All the strings of words are unique.


"""

"""
# Basic and moderately efficient algorithm (Leetcode ~47-50%)

Moderately efficient.

### Implementation note
- Simple trie implementation.
- DFS:
    - backtracking
    - filtering of visited items with a set.
    - passing down the current string and position of its final character.
    - upon first discovery of a terminal marker in the trie the string leading to it is registered 
    and the marker is removed to avoid potential multiple discovery.

### Possible alternative implementation without much consequence. 
- instead of a set to track visited cells, mark them with an invalidating flag that is removed upon backtracking.

    value = board[row][col]
    board[row][col] = FLAG
    discovery(row, col, node)
    board[row][col] = value

- 
"""
def trie_insert(root, word):
    cur = root
    i = 0
    N = len(word)
    while i < N:
        ch = word[i]
        if ch not in cur: 
            break
        cur = cur[ch]
        i += 1
    while i < N:
        ch = word[i]
        cur[ch] = {}
        cur = cur[ch]
        i += 1
    cur['*'] = {}

def find_words(board, words):
    m = len(board)
    n = len(board[0])

    # populate trie
    trie = {}
    for w in words:
        trie_insert(trie, w)

    res = []
    visited = set()
    def bt(r, c, s, node):
        if '*' in node:
            res.append(s)
            node.pop('*') # prevent dupes
            if not node: return
        for nxt_r, nxt_c in ((r, c-1), (r, c+1), (r-1, c), (r+1, c)):
            if nxt_r < 0 or nxt_r >= m or nxt_c < 0 or nxt_c >= n : continue
            if (nxt_r, nxt_c) in visited: continue
            char =  board[nxt_r][nxt_c]
            if char not in node: continue
            visited.add((nxt_r, nxt_c))
            bt(nxt_r, nxt_c, s+char, node[char])
            visited.remove((nxt_r, nxt_c))

    for r in range(m):
        for c in range(n):
            char = board[r][c]
            if char in trie:
                visited.add((r,c))
                bt(r,c, char, trie[char])
                visited.remove((r,c))
    return res

"""
# More efficient
### Key Insights (about tries)
- A smaller trie makes eliminating invalid board cells faster. So as a word is discovered it's removed, thus shrinking the overall structure. 
- It's possible to significantly augment dict-based tries.

### Secondary insights
- some optimization opportunities can be found in accessory data structures and their utilization.
- caching cell's neighbors results in a significant boost in performance.
- storing a word in reverse order in the trie based on the lesser frequency of its last character on the board resulted in a significant boost. 
"""

def find_words(board, words):
    m = len(board)
    n = len(board[0])

    def make_trie(words, char_count):
        """
        Words are store forward or backward depending on first and last characters frequencies.
        """
        trie_root = {'<':None}
        for ow in words: # ow: original word
            node = trie_root
            if char_count[ow[0]] > char_count[ow[-1]]:
                w = ow[::-1]
            i = 0
            N = len(w)
            while i < N:
                char = w[i]
                if char not in node: break
                node = node[char]
                i += 1
            while i < N:
                char = w[i]
                node[char] = {'<':node}
                node = node[char]
                i += 1
            node['*'] = w
            node['@'] = ow
        return trie

    char_count = collections.Counter(ch for row in board for ch in row)
    trie_root = make_trie(words, char_count)

    def neighbors(r,c):
        try:
            return neighbors.memo[(r,c)]
        except KeyError:
            neighbors.memo[(r,c)] = []
            for nxt_r, nxt_c in ((r, c-1), (r, c+1), (r-1, c), (r+1, c)):
                if nxt_r < 0 or nxt_r >= m or nxt_c < 0 or nxt_c >= n : continue
                neighbors.memo[(r,c)].append((nxt_r, nxt_c))
            return neighbors.memo[(r,c)]
    neighbors.memo = {}

    path = []
    res = []
    def bt(r,c,n):
        if '*' in n:
            res.append(n.pop('@'))
            w = n.pop('*')
            node = n
            while path and not node:
                ch, pre = path.pop()

            for ch in reversed(w):
                if len(node) > 1: break
                node = node['<']
                node.pop(ch)
        for nxt_r, nxt_c in neighbors(r,c):
            char = board[nxt_r][nxt_c]
            if char not in n: continue
            board[nxt_r][nxt_c] = '#'
            path.append((char, n))
            bt(nxt_r, nxt_c, n[char])
            path.pop()
            board[nxt_r][nxt_c] = char
        return False

    for r in range(m):
        for c in range(n):
            char = board[r][c]
            if char not in trie_root: continue
            board[r][c] = '#'
            path.append((char, trie_root))
            bt(r,c,trie_root[char])
            path.clear()
            board[r][c] = char
    return res

"""
A simple trie and a different approach to deleting words from it. 
"""

def make_trie(words, char_count):
    """
    Words are store forward or backward depending on first and last characters frequencies.
    """
    trie_root = {}
    for ow in words: # ow: original word
        node = trie_root
        w = ow[::-1] if char_count[ow[0]] > char_count[ow[-1]] else ow
        i, N = 0, len(ow)
        while i < N:
            char = w[i]
            if char not in node: break
            node = node[char]
            i += 1
        while i < N:
            char = w[i]
            node[char] = {}
            node = node[char]
            i += 1
        node['*'] = ow
    return trie_root


def find_words(board, words):
    m = len(board)
    n = len(board[0])

    char_count = collections.Counter(ch for row in board for ch in row)
    trie_root = make_trie(words, char_count)


    def neighbors(r,c):
        try:
            return neighbors.memo[(r,c)]
        except KeyError:
            neighbors.memo[(r,c)] = []
            for nxt_r, nxt_c in ((r, c-1), (r, c+1), (r-1, c), (r+1, c)):
                if nxt_r < 0 or nxt_r >= m or nxt_c < 0 or nxt_c >= n : continue
                neighbors.memo[(r,c)].append((nxt_r, nxt_c))
            return neighbors.memo[(r,c)]
    neighbors.memo = {}

    path = []
    visited = set()
    res = []
    def bt(r,c,n):
        if '*' in n:
            res.append(n.pop('*'))
            cur = n
            while path and not cur:
                ch, pre = path.pop()
                pre.pop(ch)
                cur = pre
            if not n: return
        cur_depth = len(path)
        for nxt_r, nxt_c in neighbors(r,c):
            char = board[nxt_r][nxt_c]
            if char not in n: continue
            if (nxt_r, nxt_c) in visited: continue
            #board[nxt_r][nxt_c] = '#'
            path.append((char, n))
            visited.add((nxt_r, nxt_c))
            bt(nxt_r, nxt_c, n[char])
            visited.remove((nxt_r, nxt_c))
            # handling path modifications, which indicates that this is probably not the best approach.
            if len(path) < cur_depth: return
            if len(path)==cur_depth: continue
            path.pop()
            #board[nxt_r][nxt_c] = char
        return False

    for r in range(m):
        for c in range(n):
            char = board[r][c]
            if char not in trie_root: continue
            #board[r][c] = '#'
            path.append((char, trie_root))
            visited.add((r,c))
            bt(r,c,trie_root[char])
            visited.clear()
            path.clear()
            #board[r][c] = char
    return res

def make_trie(words, char_count):
    trie_root = {}
    for ow in words: # ow: original word
        node = trie_root
        w = ow[::-1] if char_count[ow[0]] > char_count[ow[-1]] else ow
        i, N = 0, len(ow)
        while i < N:
            char = w[i]
            if char not in node: break
            node = node[char]
            i += 1
        while i < N:
            char = w[i]
            node[char] = {}
            node = node[char]
            i += 1
        node['*'] = ow
    return trie_root

def find_words(board, words):
    m = len(board)
    n = len(board[0])

    char_count = collections.Counter(ch for row in board for ch in row)
    trie_root = make_trie(words, char_count)

    def neighbors(r,c):
        try:
            return neighbors.memo[(r,c)]
        except KeyError:
            neighbors.memo[(r,c)] = []
            for nxt_r, nxt_c in ((r, c-1), (r, c+1), (r-1, c), (r+1, c)):
                if nxt_r < 0 or nxt_r >= m or nxt_c < 0 or nxt_c >= n : continue
                neighbors.memo[(r,c)].append((nxt_r, nxt_c))
            return neighbors.memo[(r,c)]
    neighbors.memo = {}

    path = []
    visited = set()
    res = []
    def bt(r,c,n):
        if '*' in n: # slight modification from the above
            res.append(n.pop('*'))
            cur = n
            # removing word
            for ch, pre in reversed(path):
                if cur: break
                pre.pop(ch)
                cur = pre
            if not n: return
        cur_depth = len(path)
        for nxt_r, nxt_c in neighbors(r,c):
            char = board[nxt_r][nxt_c]
            if char not in n: continue
            if (nxt_r, nxt_c) in visited: continue
            path.append((char, n))
            visited.add((nxt_r, nxt_c))
            bt(nxt_r, nxt_c, n[char])
            visited.remove((nxt_r, nxt_c))
            path.pop()
        return False

    for r in range(m):
        for c in range(n):
            char = board[r][c]
            if char not in trie_root: continue
            path.append((char, trie_root))
            visited.add((r,c))
            bt(r,c,trie_root[char])
            visited.clear()
            path.clear()
    return res
