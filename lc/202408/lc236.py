"""
# LC 236: Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



Example 1:

                   3
                  / \
                 /   \
                5     1
               / \   / \
              6   2 0   8
                 / \
                7   4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

                   3
                  / \
                 /   \
                5     1
               / \   / \
              6   2 0   8
                 / \
                7   4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1


Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""

from .bt import maketree, Node
from typing import List


def lca1(node:Node|None, p:Node, q:Node) -> Node|None:
    if not node:
        return None
    if node==p or node==q:
        return node
    left = lca1(node.left, p, q)
    right = lca1(node.right, p, q)
    if left and right:
        return node
    return left or right or None


def lca2(node:Node, p:Node, q:Node) -> Node|None:
    stack: List[tuple[Node|None, bool]] = [(node, False)]
    result = []
    while stack:
        n, visited = stack.pop()
        if n is None or n==q or n==p:
            result.append(n)
            continue
        if visited:
            left = result.pop()
            right = result.pop()
            if left and right:
                return n
            result.append(left or right or None)
        else: # not visited
            stack.append((n, True))
            stack.append((n.left, False))
            stack.append((n.right, False)) 
    return result[0]

# counting discoveries
def lca(root, p, q):
    found = []
    res = [None]
    def helper(n):
        if not n: return
        found0 = len(found)         # how many node currently found as the call starts.
        pq = n==p or n==q
        if pq:
            found.append(1)
            if len(found)==2: return
        helper(n.left)
        if len(found)==2:
            if pq:
                res[0] = n
            return
        found1 = len(found) - found0 # between pq and left leg, was any node found?
        helper(n.right)
        if len(found)==2:
            if found1:               # if a node was found then, lca is current node.
                res[0] = n
            return
    helper(root)
    return res[0]

# backtracking solution (find two linked-lists and see where they last intersect).
def lca(root, p, q):
    l1 = [root] # running list 
    l2 = []     # recording list
    res = [None]
    def bt(n):
        if n==p or n==q:    # item found.
            if not l2:      # if first list not recorded, do so now.
                l2.extend(l1)
            else:           # else search ends.
                n = min(len(l1), len(l2))
                i = 0
                while i < n and l1[i]==l2[i]: # find index of last common ancestor
                    i += 1
                res[0] = l1[i-1]
                return
        # discovery continues
        for c in (n.left, n.right):
            if res[0]: return   # discovery stops if we have a result.
            if not c:  continue # skip nil nodes
            l1.append(c)
            bt(c)
            l1.pop()
    bt(root)
    return res[0]

print(lca1(maketree([3,5,1,6,2,0,8,None,None,7,4]), Node(5), Node(1)))
print(lca1(maketree([3,5,1,6,2,0,8,None,None,7,4]), Node(5), Node(4)))
print(lca1(maketree([1,2]), Node(1), Node(2)))

print(lca_iter(maketree([3,5,1,6,2,0,8,None,None,7,4]), 5, 1).val)
print(lca_iter(maketree([3,5,1,6,2,0,8,None,None,7,4]), 5, 4).val)
print(lca_iter(maketree([1,2]), 1, 2).val)
