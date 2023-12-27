"""
LC 006 : Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"



Constraints:

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000

"""
# 44 - 06

# Intuitive, but not efficient.
def convert1(s, rcount):
    n = len(s)
    if rcount==1 or rcount==n: return s
    rows = [[] for _ in range(rcount)]
    i = 0
    while i < n:
        # fill downward
        for r in rows:
            if i >= n: break
            r.append(s[i])
            i += 1
        # fill upward (O(N^2))
        for j in range(rcount-2, 0, -1):
            if i >= n: break
            for k, r in enumerate(rows):
                r.append(s[i] if k==j else '')
            i += 1
    return ''.join(''.join(r) for r in rows)


# Efficient, but relies too much on the math behind the pattern.
def convert2(s, rows):
    n = len(s)
    if rows==1 or rows==n: return s
    seq = 2*rows - 2
    rv = []
    for r in range(rows):
        i = r
        while i<n:
            rv.append(s[i])
            if r>0 and r<rows-1:
                j = i+seq-(2*r)
                if j>=n: break
                rv.append(s[j])
            i+=seq
    return ''.join(rv)

def convert3(s, rcount):
    n = len(s)
    if rcount==1 or rcount==n: return s
    rows = [[] for _ in range(rcount)]
    i, j = 0, 1
    for char in s:
        rows[i].append(char)
        i += j
        if i==0:
            j = 1
        elif i==rcount-1:
            j = -1
    return ''.join(''.join(r) for r in rows)

s = "PAYPALISHIRING"
numRows = 3
rv1 = convert1(s, numRows)
rv2 = convert2(s, numRows)
rv3 = convert3(s, numRows)
print(rv1)
print(rv2)
print(rv3)
assert rv1=="PAHNAPLSIIGYIR"
assert rv2=="PAHNAPLSIIGYIR"
assert rv3=="PAHNAPLSIIGYIR"

s = "PAYPALISHIRING"
numRows = 4
rv1 = convert1(s, numRows)
rv2 = convert2(s, numRows)
rv3 = convert3(s, numRows)
print(rv1)
print(rv2)
print(rv3)
assert rv1=="PINALSIGYAHRPI"
assert rv2=="PINALSIGYAHRPI"
assert rv3=="PINALSIGYAHRPI"

s = "A"
numRows = 1
rv1 = convert1(s, numRows)
rv2 = convert2(s, numRows)
rv3 = convert3(s, numRows)
print(rv1)
print(rv2)
print(rv3)
assert rv1=="A"
assert rv2=="A"
assert rv3=="A"

s = "ABC"
numRows = 1
rv1 = convert1(s, numRows)
rv2 = convert2(s, numRows)
rv3 = convert3(s, numRows)
print(rv1)
print(rv2)
print(rv3)
assert rv1=="ABC"
assert rv2=="ABC"
assert rv3=="ABC"

"""
Insights:
    - Be very observant of boundary conditions. Althouhg some solutions remain cogent and They can be ambiguous in some solutions. In this problem, when `rows`==1 or `rows==len(s)` it's not possible to use the row to infer a direction. In such cases, it might be better to explicitly make these special condition and return a value for it.

    - Although an intricate pattern may be observed that may be resolved mathematically, this is rarely the best avenue in this type of problems (see solution 2).

    - The way the data structure is used in the end can be a better indicator of how it should be used during the problem resolution, much more than what the problem statement nudges you toward. In this case, the description steers you toward a 2-D table structure, where rows are filled diagonally on the way up. It may induce one to think that filling values are necessary (see the filling empty strings in solution 1). Observing that those filling values are actually useless as the return value is resolved, reveals the zigzag as more vertical both down and up. Which changes how the solution can be approached (see final solution).
"""
