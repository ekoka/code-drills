"""
LC 427: Construct Quad Tree

Given a `n * n` matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

    val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
    isLeaf: True if the node is a leaf node on the tree or False if the node has four children.

class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}

We can construct a Quad-Tree from a two-dimensional area using the following steps:

    If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
    If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
    Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

You don't need to read this section for solving the problem. This is only if you want to understand the output format here. The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.



Example 1:

Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.

Example 2:

Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:



Constraints:

    n == grid.length == grid[i].length
    n == 2^x where 0 <= x <= 6
"""
# 05
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

def solution(grid):
    N = len(grid)
    def sol(grid, i, j, x, y):
        if j-i==1:
            return Node(val=grid[i][x], isLeaf=True)
        # top, right, bottom, left
        a = (j+i)//2
        b = (y+x)//2
        tl = sol(grid, i, a, x, b)
        tr = sol(grid, i, a, b, y)
        bl = sol(grid, a, j, x, b)
        br = sol(grid, a, j, b, y)
        same_value = lambda a, b, c, d: a.val==b.val==c.val==d.val
        if all(n.isLeaf for n in (tl, tr, bl, br)) and same_value(tl, tr, bl, br):
            return Node(tl.val, True)
        return Node(0, False tl, tr, bl, br)
    return sol(grid, 0, N, 0, N)

def solution(grid):
    N = len(grid)
    def sol(i, j, x, y):
        if j-i==1:
            return Node(val=grid[i][x], isLeaf=True)
        # top, right, bottom, left
        mid_row = (j+i) >> 1
        mid_col = (y+x) >> 1
        a = sol(i, mid_row, x, mid_col)
        b = sol(i, mid_row, mid_col, y)
        c = sol(mid_row, j, x, mid_col)
        d = sol(mid_row, j, mid_col, y)
        n = Node(a.val, a.isLeaf and b.isLeaf and c.isLeaf and d.isLeaf and
            a.val==b.val==c.val==d.val)
        if not n.isLeaf:
            n.topLeft, n.topRight, n.bottomLeft, n.bottomRight =  a, b, c, d
        return n
    return sol(0, N, 0, N)


def solution(grid):
    N = len(grid)
    stack = [(0,N,0,N,False)]
    result = []
    while stack:
        i, j, x, y, visited = stack.pop()
        if j-i==1:
            result.append(Node(val=grid[i][x], isLeaf=True))
            continue
        if not visited:
            stack.append((i, j, x, y, True))
            # top, right, bottom, left
            mid_row = (j+i) >> 1
            mid_col = (y+x) >> 1
            stack.append((i, mid_row, x, mid_col, False))
            stack.append((i, mid_row, mid_col, y, False))
            stack.append((mid_row, j, x, mid_col, False))
            stack.append((mid_row, j, mid_col, y, False))
            continue
        a = result.pop()
        b = result.pop()
        c = result.pop()
        d = result.pop()
        if (a.isLeaf and b.isLeaf and c.isLeaf and d.isLeaf and
            a.val==b.val==c.val==d.val):
            result.append(Node(a.val, True))
        else:
            result.append(Node(0, False, a, b, c, d))
    return result[0]

def quadtree(grid) -> 'Node':
    N = len(grid)
    for r in range(N):
        for c in range(N):
            grid[r][c] = Node(grid[r][c]==1, True, None, None, None, None)
    while N > 1:
        new_grid = []
        for r in range(0, N, 2):
            new_grid.append([])
            for c in range(0, N, 2):
                topLeft = grid[r][c]
                topRight = grid[r][c+1]
                bottomLeft = grid[r+1][c]
                bottomRight = grid[r+1][c+1]
                allLeaves = topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf
                v = topLeft.val
                if (allLeaves and v==topRight.val and v==bottomLeft.val and v==bottomRight.val):
                    new_grid[-1].append(Node(topLeft.val, True, None, None, None, None))
                else:
                    new_grid[-1].append(Node(False, False, topLeft, topRight, bottomLeft, bottomRight))
        grid = new_grid
        N = len(grid)
    return grid[0][0]

grid = [[0,1],[1,0]]
print(solution(grid))
#Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]

grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
print(solution(grid))
#Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
