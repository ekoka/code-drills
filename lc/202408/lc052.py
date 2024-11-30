"""
LC 052: N-Queens II
"""
# 43

def total_nqueens(n):
    columns, ltr, rtl = ([False]*n, [False] * (2*n), [False] * (2*n))
    res, combo = [0], [0]
    def dfs(row):
        if combo[0]==n:
            res[0] += 1
            return
        for col in range(n):
            i, j = n-1-row+col, row+col
            if columns[col] or ltr[i] or rtl[j]: continue
            columns[col], ltr[i], rtl[j] = True, True, True
            combo[0] += 1
            dfs(row+1)
            combo[0] -= 1
            columns[col], ltr[i], rtl[j] = False, False, False
    for col in range(n):
        i = n+col-1
        columns[col], ltr[i], rtl[col] = True, True, True
        combo[0] = 1      
        dfs(1)
        combo[0] = 0
        columns[col], ltr[i], rtl[col] = False, False, False
    return res[0]

def total_nqueens(n):
    columns, ltr, rtl = ([False]*n, [False] * (2*n), [False] * (2*n))
    res, combo = [0], [0]
    def dfs(row):
        if combo[0]==n:
            res[0] += 1
            return
        for col in range(n):
            i, j = n-1-row+col, row+col
            if columns[col] or ltr[i] or rtl[j]: continue
            columns[col], ltr[i], rtl[j] = True, True, True
            combo[0] += 1
            dfs(row+1)
            combo[0] -= 1
            columns[col], ltr[i], rtl[j] = False, False, False
    dfs(0)
    return res[0]


def total_nqueens(n):
    columns, ltr, rtl = ([False]*n, [False] * (2*n), [False] * (2*n))
    res = 0
    for start in range(n):
        stack = [(0, start, n-1+start, start, False)]
        combo = 0
        while stack:
            row, col, i, j, bt = stack.pop()
            if bt:
                combo -= 1
                columns[col], ltr[i], rtl[j] = False, False, False
                continue
            stack.append((row, col, i, j, True))
            columns[col], ltr[i], rtl[j] = True, True, True
            combo += 1
            if combo==n:
                res += 1
                continue
            nxt_row = row + 1
            for c in range(n):
                x = n-1 - nxt_row + c
                y = nxt_row + c
                if columns[c] or ltr[x] or rtl[y]: continue
                stack.append((nxt_row, c, x, y, False))
    return res

# doesn't seem to make much of a difference
def total_nqueens(n):
    available_columns = {c for c in range(n)}
    columns, ltr, rtl = ([False]*n, [False] * (2*n), [False] * (2*n))
    res = 0
    for start in range(n):
        stack = [(0, start, n-1+start, start, False)]
        combo = 0
        while stack:
            row, col, i, j, bt = stack.pop()
            if bt:
                combo -= 1
                columns[col], ltr[i], rtl[j] = False, False, False
                available_columns.add(col)
                continue
            stack.append((row, col, i, j, True))
            available_columns.remove(col)
            columns[col], ltr[i], rtl[j] = True, True, True
            combo += 1
            if combo==n:
                res += 1
                continue
            nxt_row = row + 1
            for c in available_columns:
                x = n-1 - nxt_row + c
                y = nxt_row + c
                if columns[c] or ltr[x] or rtl[y]: continue
                stack.append((nxt_row, c, x, y, False))
    return res
"""
# Handling the diagonals

- Before placing a queen, we must ensure that no previous queen is already controlling the diagonals on that position.
- One approach to do this is to "activate" diagonal "ancestor" positions on the vertical or horizontal grid edges whenever a new queen is placed.
- Two such diagonals ancestor positions must be verified: Left-to-Right and Right-to-Left.

    e.g. 
    - When point x on the grid is at (4, 1) LtR diagonal ancestor is (3, 0), while RtL is (0, 5).
    - When x is at (2, 4), LtR is (0, 2) and RtL is (0, 6).
    - When x is at (4, 5), LtR is (0, 1) and RtL is (3, 6).
    - When x is at (6, 2), LtR is (4, 0) and RtL is (2, 6).

                RtL        LtR     RtL    LtR                   
                 |          |       |      |        
       0 1 2 3 4 5 6    0 1 2 3 4 5 6    0 1 2 3 4 5 6        0 1 2 3 4 5 6
       1 . . . . . .    1 . . . . . .    1 . . . . . .        1 . . . . . .
       2 . . . . . .    2 . . . x . .    2 . . . . . .        2 . . . . . . --RtL
 LtR-- 3 . . . . . .    3 . . . . . .    3 . . . . . . --RtL  3 . . . . . . 
       4 x . . . . .    4 . . . . . .    4 . . . . x .  LtR-- 4 . . . . . .
       5 . . . . . .    5 . . . . . .    5 . . . . . .        5 . . . . . .
       6 . . . . . .    6 . . . . . .    6 . . . . . .        6 . x . . . .

- The positions to check are on the grid's three outer edges, either on the vertical left-most (i.e the first column), the horizontal top-most (first row), or the vertical right-most (last column).
- We could thus have 2 arrays per diagonals (left vertical + top horizontal for Left-to-Right; and top horizontal and right vertical for Right-to-Left).
- However, it's also possible to join each diagonal array set into a single array by applying a  position to index conversion.

- e.g. For the Left-to-Right diagonal, we normally use the left-most column and top-most row.

But we can unify the positions into a single array.

    [0 .. 6] + [0 .. 6] -> [0 .. 12]

## Left-to-Right Diagonal

### Convert from positions on first column

    row index   |  diagonal index
    -----------------------------
        0       |  n-1
        1       |  n-2
        2       |  n-3
        ...     |
        n-3     |   2                    
        n-2     |   1                    
        n-1     |   0                    

- relationship 
    (r, 0)  -> n-1 - r      // with r going from  0 to n-1
            
            => r = 0    -> n-1 - 0      =   n-1
            => r = 1    -> n-1 - 1      =   n-2
            => r = 2    -> n-1 - 2      =   n-3
            ...
            => r = n-3  -> n-1 - (n-3)  =   2
            => r = n-2  -> n-1 - (n-2)  =   1
            => r = n-1  -> n-1 - (n-1)  =   0

### Convert from positions on first row (top horizontal)
- remember that on the first columns, the last diagonal index after conversion was n-1. That's also the offset when converting from top row positions.
    
    col index   | diagonal index
    ----------------------------
        0       |  n-1
        1       |  n
        2       |  n+1
        3       |  n+2
        ...     |
        n-3     |  n+(n-4)
        n-2     |  n+(n-3)
        n-1     |  n+(n-2)

- relationship

    (0, c)  -> n-1 + c      // with c going from  0 to n-1

            => c = 0    -> n-1
            => c = 1    -> n
            => c = 2    -> n+1
            => c = 3    -> n+2
            ...
            => c = n-1  -> n-1 + (n-1) = 2n - 2


### Unified formula to convert first column and first row coordinates to their corresponding
index inside a single array:

    (r, c)  => (n-1) - r + c   => n - 1  - r + c

### This formula remains consistent over the entire grid. 
#### Proof 1
The relationship of an arbitrary position `(i, j)` on the grid to its earliest diagonal ancestor `(r, c)` is:

        (r, c) -> (r+x, c+x) = (i, j)

That is, both the vertical and horizontal axes of the ancestor must be offset by exactly the same amount `x` to get to a diagonal descendant. Conversely, `x` must be removed from the descendant's vertical and horizontal coordinates to get to its ancestor. So, the formula to get to an ancestor `(r, c)` from its descendant point `(i, j)` in the grid is 

        (i, j) -> (i-x, j-x) = (r, c)

Let's rewrite the relationship between the diagonal ancestors on the grid with their index on the array in terms of i and j:

    (r, c)      -> n - 1  + r + c
    (i-x, j-x)  -> n - 1 - (i-x) + (j-x) = n - 1 - i + x + j - x = n - 1 - i + j

This means that if we have a point (i, j) and we want to determine its index on the single diagonal array, we don't need to first convert it to its ancestor (r, c) on the grid. We can simply apply the formula `(i, j) -> n - 1 - i + j`, which is equivalent to the original formula `(r, c) -> n - 1 - r + c`.

#### Proof2
Consider an arbitrary position (i, j) on the grid.
    
    if i > j:   // i.e. column is closer to the edge
        // Find diagonal ancestor coordinates on first column by offsetting columns by j
        (i, j)   -> (i-j, j-j) ->  (i-j, 0)
        // now apply the formula to translate ancestor's coordinate to index on diagonal array
        (i-j, 0)    -> n - 1 - (i-j) =  n - 1 - i + j
    else:       // row is closer to the edge
        // offset by rows to find coordinate on first row
        (i, j)  -> (0, j-i)
        // applying the formula
        (0, j-i)    -> n - 1 + (j-i) =  n - 1 - i + j

The formula for the two cases is the same and is equivalent to the original formula. 

         (r, c) -> n - 1 - r + c
         (i, j) -> n - 1 - i + j

-----

# Right to left

## when row = 0

    col index   |  diagonal index
    -----------------------------
        0       |  0
        1       |  1
        2       |  2
        ...     |
        n-1     | n-1                   

- relationship 

    (0, c)  ->  c   // with c going from  0 to n-1
            
## When col = n-1
    
    row index   | diagonal index
    ----------------------------
        1       |  n 
        2       |  n + 1
        3       |  n + 2
        ...     |
        n-3     |  n + (n-4)
        n-2     |  n + (n-3)
        n-1     |  n + (n-2)

- relationship

    (n-1, r)  -> n + r - 1  // with r going from  1 to n-1

### General formula to convert first row and last column coordinates to their corresponding
index in right-to-left array:

    (r, c)       -> r + c

### Calculating R-to-L diagonal positions
    
    if r > n - 1 - c:   // if column is closer to the edge
        // offset by columns to find row coordinate on last column
        (r,c) -> (r - (n-c-1), n-1)
        // now use formula to find index in RtL diagonal array
        (r - (n-c-1), n-1) -> r - n + c + 1  + n - 1 =  r + c
    else:               // if row is closer to the edge 
        // offset by rows to find column coordinate on first row
        (r,c) -> (0, c+r)
        // apply formula
        (0, c+r)    ->  c + r 

"""
