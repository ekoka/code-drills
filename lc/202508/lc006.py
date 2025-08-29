"""
string convert(string s, int numRows);

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Input: s = "A", numRows = 1
Output: "A"

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

def convert(s, numRows):
    if numRows==1: return s
    if numRows==len(s): return s
    rows = [[] for _ in range(numRows)]
    i = 0
    step = 1
    for c in s:
        rows[i].append(c)
        i += step
        if i==0:
            step = 1 
        elif i==numRows-1:
            step = -1
    return "".join("".join(row) for row in rows)

def convert(s, numRows):
    n = len(s)
    if numRows==1 or numRows==n: return s
    rows = [""] * numRows
    row_index = zigzag(n, numRows)
    for i in range(n):
        rows[row_index[i]] += s[i]
    return "".join(rows)


def zigzag(n, rowcount):
    res = [None] * (n + 2*rowcount)
    i = 0
    while i < n:
        for j in range(rowcount):
            res[i] = j
            i += 1
        for j in range(rowcount-2, 0, -1):
            res[i] = j
            i += 1
    return res

def convert(s, numRows):
    if numRows==1 or numRows==len(s): return s
    rows = [""] * numRows
    i = 0
    step = 1
    for c in s:
        rows[i] += c
        i += step
        if i==0:
            step = 1 
        elif i==numRows-1:
            step = -1
    return "".join(rows)

s = "PAYPALISHIRING"
numRows = 3
exp = "PAHNAPLSIIGYIR"
res = convert(s, numRows)
print(res)
assert res==exp

s = "PAYPALISHIRING" 
numRows = 4
exp = "PINALSIGYAHRPI"
res = convert(s, numRows)
print(res)
assert res==exp

s = "A"
numRows = 1
exp = "A"
res = convert(s, numRows)
print(res)
assert res==exp

s = "AB"
numRows = 1
exp = "AB"
res = convert(s, numRows)
print(res)
assert res==exp
