"""
LC 072: Edit Distance

Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

    0 <= word1.length, word2.length <= 500
    word1 and word2 consist of lowercase English letters.
"""

def edit_distance_recursive(word1, word2):
    n1 = len(word1)
    n2 = len(word2)
    def helper(i, j):
        if i==n1: return n2 - j
        if j==n2: return n1 - i
        
        sub = helper(i+1, j+1)
        if word1[i]==word2[j]:
            return sub
        
        ins = helper(i+1, j) # insertion
        dlt = helper(i, j+1) # deletion
        return min(ins, dlt, sub) + 1
    return helper(0, 0)

def edit_distance(word1, word2):
    memo = [ [0] * (len(word2)+1) for _ in range(len(word1)+1)]
    for i in range(1, len(word2)+1):
        memo[0][i] = i
    for j in range(1, len(word1)+1):
        memo[j][0] = j
    for i in range(1, len(word1)+1):
        for j in range(1, len(word2)+1):
            if word1[i-1]==word2[j-1]: # only check previous match
                memo[i][j] = memo[i-1][j-1]
            else: # check all previous versions
                memo[i][j] = min(memo[i-1][j], memo[i][j-1], memo[i-1][j-1]) + 1
    return memo[-1][-1]

def edit_distance(word1, word2):
    n2 = len(word2) + 1
    pre = [i for i in range(n2))
    cur = [None] * n2
    for i in range(1, len(word1)+1):
        cur[0] = pre[0] + 1
        for j in range(1, n2):
            if word1[i-1]==word2[j-1]:
                cur[j] = pre[j-1]
            else:
                cur[j] = min(pre[j], cur[j-1], pre[j-1]) + 1
        pre, cur = cur, pre
    return pre[-1]

def edit_distance_bfs(word1, word2):
    n1 = len(word1)
    n2 = len(word2)
    stack = [(0,0)]
    discovered = [ [False] * (n2+1) for _ in range(n1+1) ]
    discovered[0][0] = True
    diffcount = 0
    while stack:
        new_stack = []
        while stack:
            i, j = stack.pop()
            while i < n1 and j < n2 and word1[i]==word2[j]:
                i += 1
                j += 1
            if i==n1 and j==n2: return diffcount
            for x,y in ((i, j+1), (i+1, j), (i+1, j+1)):
                if x <= n1 and y <= n2 and not discovered[x][y]:
                    new_stack.append((x,y))
                    discovered[x][y] = True
        diffcount += 1
        stack = new_stack


