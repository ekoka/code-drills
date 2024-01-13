"""
LC 102: Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

       3
      / \
     9   20
        /  \
       15   7

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []



Constraints:

    The number of nodes in the tree is in the range [0, 2000].

    -1000 <= Node.val <= 1000

"""

from .bt import maketree
from collections import deque

def lot(root):
    if not root: return []
    stack = [root]
    res = []
    while stack:
        res.append(list(stack))
        stack = [c for n in stack for c in (n.left, n.right) if c]
    return res

print(lot(maketree([3,9,20,None,None,15,7])))
print(lot(maketree([1])))
print(lot(maketree([])))
print(lot_with_queue(maketree([3,9,20,None,None,15,7])))
print(lot_with_queue(maketree([1])))
print(lot_with_queue(maketree([])))
