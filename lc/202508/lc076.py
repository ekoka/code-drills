"""
LC 76: Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

Constraints:

    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
from collections import Counter
MAXINT = float('inf')

def minwin(s, t):
    m = len(s)
    n = len(t)

    needle_count = {c:0 for c in t}
    win_count = {**needle_count} # copy
    missing = {*needle_count}
    for c in t:
        needle_count[c] += 1

    start = 0
    end = 0

    rec = [0, MAXINT]

    while end < m:
        if s[end] in win_count:
            win_count[s[end]] += 1
            if s[end] in missing and win_count[s[end]]==needle_count[s[end]]:
                missing.remove(s[end])
        if missing: 
            end += 1
            continue
        if end==m: break
        while not missing:
            if end+1-start < rec[1]-rec[0]:
                rec = [start, end+1]
            if s[start] in win_count:
                win_count[s[start]] -= 1
                if win_count[s[start]] < needle_count[s[start]]:
                    missing.add(s[start])
            start += 1
        end += 1
    return "" if rec[1]-rec[0]==MAXINT else s[rec[0]:rec[1]]
    
def minwin(s, t):
    m = len(s)
    n = len(t)

    needle_count = Counter(t)
    win_count = {k:0 for k in needle_count} # copy
    missing = len(win_count)

    start = 0
    end = 0

    rec = (0, MAXINT)

    while end < m:
        if s[end] in win_count:
            win_count[s[end]] += 1
            if win_count[s[end]]==needle_count[s[end]]:
                missing -= 1
        if missing:
            end += 1
            continue
        if end==m: break
        while not missing:
            if end+1-start < rec[1]-rec[0]:
                rec = (start, end+1)
            if s[start] in win_count:
                win_count[s[start]] -= 1
                if win_count[s[start]] < needle_count[s[start]]:
                    missing += 1
            start += 1
        end += 1
    return "" if rec[1]-rec[0]==MAXINT else s[rec[0]:rec[1]]

def minwin(s, t):
    m = len(s)
    n = len(t)

    needle_count = Counter(t)
    win_count = {k:0 for k in needle_count.keys()} # copy
    missing = len(win_count)

    start = 0
    end = 0

    rec = (0, MAXINT)

    while end < m:
        if s[end] in win_count:
            win_count[s[end]] += 1
            if win_count[s[end]]==needle_count[s[end]]:
                missing -= 1
        while not missing:
            if s[start] not in win_count:
                start += 1
                continue
            win_count[s[start]] -= 1
            if win_count[s[start]] < needle_count[s[start]]:
                if end+1-start < rec[1]-rec[0]:
                    rec = (start, end+1)
                missing += 1
            start += 1
        end += 1
    return "" if rec[1]-rec[0]==MAXINT else s[rec[0]:rec[1]]

s = "ADOBECODEBANC"
t = "ABC"
exp = "BANC"
res = minwin(s, t)
print(res)
assert exp==res

s = "a"
t = "a"
exp = "a"
res = minwin(s, t)
print(res)
assert exp==res

s = "a"
t = "aa"
exp = ""
res = minwin(s, t)
print(res)
assert exp==res

s = "abc"
t = "ac"
exp = "abc"
res = minwin(s, t)
print(res)
assert exp==res

