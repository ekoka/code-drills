"""
LC 098: Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

        2
       / \
      1   3

Input: root = [2,1,3]
Output: true

Example 2:

      5
     / \
    1   4
       / \
      3   6

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

MIN = -231
MAX = 230

def validate_bst(root, m=MIN, M=MAX):
    if not root: return True
    if root.val < m:
        return False
    if root.val > M:
        return False
    return validate_bst(root.left, m, root.val) and\
            validate_bst(root.left, root.val, M)

def validate_bst(root):
    def helper(n, minval, maxval):
        if not n: return True
        if n.val>=maxval:
            return False
        if n.val<=minval:
            return False
        return helper(n.left, minval, n.val) and\
                helper(n.right, n.val, maxval)
    inf = float('inf')
    return helper(n, -inf, inf)

def validate_bst_iterative(root):
    stack = [(root, MIN, MAX)]
    while stack:
        node, m, M = stack.pop()
        if not node:
            continue
        if node.val < m:
            return False
        if node.val > M:
            return False
        stack.append((root.left, m, root.val))
        stack.append((root.right, root.val, M))
    return True

def validate_bst(root):
    inf = float('inf')
    stack = [(root, inf, -inf)]
    while stack:
        n, minval, maxval = stack.pop()
        if not n: continue
        if n.val>=maxval:
            return False
        if n.val<=minval:
            return False
        stack.append(n.left, minval, n.val) 
        stack.append(n.right, n.val, maxval)
    return True

def validate_bst_2(root):
    pre = [float('-inf')]
    def helper():
        if not root:
            return True
        if not helper(root.left):
            return False 
        if pre[0] >= root.val:
            return False
        pre[0] = root.val
        return helper(root.right):
    return helper(root)

def validate_bst(root):
    stack = []
    nxt = root
    pre = float('-inf')
    while nxt:
        while nxt:
            stack.append(nxt)
            nxt = nxt.left
        while stack:
            n = stack.pop()
            if pre >= n.val:
                return False
            pre = n.val
            if n.right:
                nxt = n.right
                break
    return True

def validate_bst(root):
    stack = []
    nxt = root
    pre = float('-inf')
    while nxt:
        while nxt:
            stack.append(nxt)
            nxt = nxt.left
        while stack and not nxt:
            n = stack.pop()
            if pre >= n.val:
                return False
            pre = n.val
            nxt = n.right
    return True

