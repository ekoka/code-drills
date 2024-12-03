"""
LC 005 : Longest Palindromic Substring

Given a string `s`, return the longest palindromic substring in `s`.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

"""
# 28

# Classic DP: We mark True all memo[start][end] positions that match a palindrome 
# and build subsequent positions using previous ones.
# The traversal of the matrix must account for that last requirement. 
def dp_solution1(s):
    n = len(s)
    # Initialize with all start:end positions as False (not palindromes)
    memo = [ [False] * n for _ in range(n) ]
    res = (0,0)
    # Mark all singles and matching duos as True
    for i in range(n-1):
        memo[i][i] = True
        if s[i]==s[i+1]:
            memo[i][i+1] = True
            if res[1]-res[0]==0:
                res = (i, i+1)
    memo[-1][-1] = True
    # Now traverse and mark other matching positions 
    for end in range(len(s)):
        for start in range(end-2, -1, -1):
            if s[start]==s[end] and memo[start+1][end-1]:
                memo[start][end] = True
                if res[1]-res[0] < end-start:
                    res = (start, end)
    return s[res[0]: res[1]+1]

def dp_solution(s):
    n = len(s)
    memo = []
    res = (0,0)
    for i in range(n):
        if i > 0 and s[i]==s[i-1]:
            memo.append([i-1, i])
            res = (i-1, i)
        else:
            memo.append([i])

    for i in range(1, n):
        for j in memo[i-1]:
            k = j-1
            if k >= 0 and s[k]==s[i]:
                memo[i].append(k)
                if i-k > res[1]-res[0]:
                    res = (k, i)
    return s[res[0]:res[1]+1]

# Also DP, but instead of tracking all positions, we only record and carry on with those that match palindromes.
# Algorithm is sligthly modified. Instead of True/False matrix, the memoization tracks all palindromes in an array 
# of arrays with the structure: [ All ending positions: [Valid starting positions] ]
def dp_solution2(s):
    n = len(s)
    # every ending position is trivially a valid starting position (a single-character palindrome).
    memo = [ [end] for end in range(n) ]
    res = (0,0)
    for end in range(1, n):
        if s[end-1]==s[end]: # matching duos
            memo[end].append(end-1)
            if res[1]-res[0]==0:
                res = (end-1, end)
        for start in memo[end-1]:
            if start > 0 and s[start-1]==s[end]:
                memo[end].append(start-1)
                if res[1]-res[0] < end-(start-1):
                    res = (start-1, end)
    return s[res[0]: res[1]+1]

def dp_solution2(s): # optimization: use one-dimension memoization.
    n = len(s)
    res = (0,0)
    pre = [0]
    for end in range(1, n):
        cur = [end]
        if s[end-1]==s[end]:
            cur.append(end-1)
            if res[1]-res[0]==0:
                res = (end-1, end)
        for start in pre:
            if start > 0 and s[start-1]==s[end]:
                cur.append(start-1)
                if res[1]-res[0] < end-(start-1):
                    res = (start-1, end)
        pre = cur
    return s[res[0]: res[1]+1]

# or using while and list popping (seems slightly less performant in Python than the above)

def dp_solution2(s): # although
    n = len(s)
    res = (0,0)
    pre = [0]
    cur = []
    for end in range(1, n):
        cur.append(end)
        if s[end-1]==s[end]:
            cur.append(end-1)
            if res[1]-res[0]==0:
                res = (end-1, end)
        while pre:
            start = pre.pop()
            if start > 0 and s[start-1]==s[end]:
                cur.append(start-1)
                if res[1]-res[0] < end-(start-1):
                    res = (start-1, end)
        pre, cur = cur, pre
    return s[res[0]: res[1]+1]

# Expand around Center
def expand_around_center_solution(s):
    n = len(s)
    def expand(i,j):
        while i >= 0 and j < n and s[i]==s[j]:
            i -= 1
            j += 1
        return i+1, j-1
    res = (0, 0)
    for i in range(n):
        even = expand(i,i+1)
        odd = expadn(i-1, i+1)
        pal = even if even[1]-even[0] > odd[1]-odd[0] else odd
        if pal[1]-pal[0] > res[1]-res[0]:
            res = pal
            if (n-i)*2 + 1 < res[1]-res[0]:
                break
    return s[res[0]:res[1]+1]

# To study
def longestPalindrome(s):
    t = '#'.join(f'^{s}$')
    n = len(t)
    P = [0] * n
    C = R = 0

    for i in range(2, n-2):
        # Find the corresponding letter in the palindrome substring
        mirr = 2*C - i
        if R > i:
            P[i] = min(R - i, P[mirr])
        
        # Expand around i
        while t[i + P[i] + 1] == t[i - P[i] - 1]:
            P[i] += 1
        
        # If palindrome centered at i expands past R, adjust center C and R
        if i + P[i] > R:
            C, R = i, i + P[i]
    
    max_len, center_index = max((n, i) for i, n in enumerate(P))
    start = (center_index - max_len) // 2
    return s[start:start + max_len]

# Binary search solution

def binary_search_solution(S):
    n = len(S)
    lo = 1
    hi = n+1
    even_palindromes = []
    odd_palindromes = []
    while lo < hi:
        m = even_middle(lo, hi)
        if m==0: break
        if even_palindromes:
            found_palins = filter_palindromes(S, m, even_palindromes)
        else:
            found_palins = discover_palindromes(S, m)
        if found_palins:
            even_palindromes = found_palins
            lo = m+2
        else:
            hi = m
    res = even_palindromes[0] if even_palindromes else (0,0)
    lo = 1
    hi = len(S)+1
    while lo < hi:
        m = odd_middle(lo, hi)
        if m==0: break
        if odd_palindromes:
            found_palins = filter_palindromes(S, m, odd_palindromes)
        else:
            found_palins = discover_palindromes(S, m)
        if found_palins:
            odd_palindromes = found_palins
            lo = m+2
        else:
            hi = m
    if odd_palindromes and odd_palindromes[0][1]-odd_palindromes[0][0] > res[1]-res[0]:
        res = odd_palindromes[0]
    return S[res[0]:res[1]+1]

def odd_middle(lo, hi):
    v = (lo + hi)//2
    if v % 2:
        return v
    return v - 1
    
def even_middle(lo, hi):
    v = (lo + hi)//2
    if v % 2:
        return v - 1
    return v

def discover_palindromes(S, size):
    rv = []
    offset = (size-1)//2
    diff = 0 if size%2 else 1 
    for i in range(offset, len(S)-diff-offset):
        j = i + diff
        while S[i]==S[j]:
            if j-i+1==size:
                rv.append((i, j))
                break
            i -= 1
            j += 1
    return rv

def filter_palindromes(S, size, palindromes):
    rv = []
    size_diff = (size - (palindromes[0][1] - palindromes[0][0]+1))//2
    for i,j in palindromes:
        if i - size_diff < 0 or j + size_diff >= len(S) : continue
        while S[i]==S[j]:
            if j-i+1==size:
                rv.append((i, j))
                break
            i -= 1
            j += 1
    return rv
"""
- try binary search for palindromes of specific even sizes.
- if we find palindromes in a size we collect them and try a larger size with the same bucket.
- try the same process for odd sized palindromes.
- return largest palindrome.
"""
def solution(S):
    n = len(S)
    even_palindromes = discover_palindromes(S, even_middle)
    odd_palindromes = discover_palindromes(S, odd_middle)
    if even_palindromes:
        lo = 1
        hi = n+1
        while hi > 2 and lo < hi:
            m = even_middle(lo, hi)
            #if m==0: break
            found_palins = filter_palindromes(S, m, even_palindromes)
            if found_palins:
                even_palindromes = found_palins
                lo = m+2
            else:
                hi = m-1
    ev = even_palindromes[0] if even_palindromes else (0,0)
    if odd_palindromes:
        lo = 1
        hi = n+1
        while hi > 3 and lo < hi:
            m = odd_middle(lo, hi)
            #if m==0: break
            found_palins = filter_palindromes(S, m, odd_palindromes)
            if found_palins:
                odd_palindromes = found_palins
                lo = m+2
            else:
                hi = m-1
    od = odd_palindromes[0] if odd_palindromes else (0,0)
    return S[ev[0]:ev[1]+1] if ev[1]-ev[0] > od[1]-od[0] else S[od[0]:od[1]+1]

def odd_middle(lo, hi):
    v = (lo + hi)//2
    if v % 2:
        return v
    return v - 1
    
def even_middle(lo, hi):
    v = (lo + hi)//2
    if v % 2:
        return v - 1
    return v

def discover_palindromes(S, middle_fnc):
    lo = 1
    hi = len(S) + 1
    def helper(size):
        rv = []
        offset = (size-1)//2
        diff = 0 if size%2 else 1 
        for i in range(offset, len(S)-diff-offset):
            j = i + diff
            while S[i]==S[j]:
                if j-i+1==size:
                    rv.append((i, j))
                    break
                i -= 1
                j += 1
        return rv
    while lo < hi:
        m = middle_fnc(lo, hi)
        if m==0: break
        found_palins = helper(m)
        if found_palins:
            return found_palins
        else:
            hi = m-1

def filter_palindromes(S, size, palindromes):
    rv = []
    size_diff = (size - (palindromes[0][1] - palindromes[0][0]+1))//2
    for i,j in palindromes:
        if i - size_diff < 0 or j + size_diff >= len(S) : continue
        while S[i]==S[j]:
            if j-i+1==size:
                rv.append((i, j))
                break
            i -= 1
            j += 1
    return rv

"""
Binary search approach (fairly efficient, comparable to brute force and better than DP).
- try binary search for palindromes of specific even sizes.
- if we find palindromes in a size we collect them and try a larger size with the same bucket.
- try the same process for odd sized palindromes.
- return largest palindrome.
"""
def solution(S):
    n = len(S)
    even_palindromes = discover_palindromes(S, even_middle)
    odd_palindromes = discover_palindromes(S, odd_middle)
    if even_palindromes:
        lo = 1
        hi = n+1
        while hi > 2 and lo < hi:
            m = even_middle(lo, hi)
            #if m==0: break
            found_palins = filter_palindromes(S, m, even_palindromes)
            if found_palins:
                even_palindromes = found_palins
                lo = m+2
            else:
                hi = m-1
    ev = even_palindromes[0] if even_palindromes else (0,0)
    if odd_palindromes:
        lo = 1
        hi = n+1
        while hi > 3 and lo < hi:
            m = odd_middle(lo, hi)
            #if m==0: break
            found_palins = filter_palindromes(S, m, odd_palindromes)
            if found_palins:
                odd_palindromes = found_palins
                lo = m+2
            else:
                hi = m-1
    od = odd_palindromes[0] if odd_palindromes else (0,0)
    return S[ev[0]:ev[1]+1] if ev[1]-ev[0] > od[1]-od[0] else S[od[0]:od[1]+1]

def odd_middle(lo, hi):
    v = (lo + hi)//2
    if v % 2:
        return v
    return v - 1
    
def even_middle(lo, hi):
    v = (lo + hi)//2
    if v % 2:
        return v - 1
    return v

def discover_palindromes(S, middle_fnc):
    lo = 1
    hi = len(S) + 1
    def helper(size):
        rv = []
        offset = (size-1)//2
        diff = 0 if size%2 else 1 
        for i in range(offset, len(S)-diff-offset):
            j = i + diff
            while S[i]==S[j]:
                if j-i+1==size:
                    rv.append((i, j))
                    break
                i -= 1
                j += 1
        return rv
    while lo < hi:
        m = middle_fnc(lo, hi)
        if m==0: break
        found_palins = helper(m)
        if found_palins:
            return found_palins
        else:
            hi = m-1

def filter_palindromes(S, size, palindromes):
    rv = []
    size_diff = (size - (palindromes[0][1] - palindromes[0][0]+1))//2
    for i,j in palindromes:
        if i - size_diff < 0 or j + size_diff >= len(S) : continue
        while S[i]==S[j]:
            if j-i+1==size:
                rv.append((i, j))
                break
            i -= 1
            j += 1
    return rv


