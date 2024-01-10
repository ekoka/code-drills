"""
LC 117 : Populating Next Right Pointer in Each Node II
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=study-plan-v2&envId=top-interview-150

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Example 1:

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:

Input: root = []
Output: []



Constraints:

    The number of nodes in the tree is in the range [0, 6000].
    -100 <= Node.val <= 100

Follow-up:
You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""

from collections import deque

class Node:
    def __init__(
            self, val: int = 0, left: 'Node|None' = None, right: 'Node|None' = None, next: 'Node|None' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect1(node):
    q = deque()
    q.append((node, 0))
    pre_level = -1
    pre  = None
    while q:
        n, level = q.popleft()
        if pre: 
            if pre_level==level:
                pre.next = n
            else:
                pre.next = None
        for c in (n.left, n.right):
            if c:
                q.append((c, level+1))
        pre = n
        pre_level = level

def connect2(node):
    if not node: return
    q = deque([node])
    while q:
        pre  = None
        next_q = deque()
        while q:
            n = q.popleft()
            for c in (n.left, n.right):
                if c:
                    next_q.append(c)
            n.next = None
            if pre:
                pre.next = n
            pre = n
        q = next_q

def connect3(node):
    if not node: return
    stack = [node]
    while stack:
        pre  = Node() # dummy node
        next_stack = []
        for n in stack:
            if n.left:
                next_stack.append(n.left)
            if n.right:
                next_stack.append(n.right)
            pre.next = n
            pre = n
        stack = next_stack

def connect4(node):
    if not node: return
    stack = [(node, 0)]
    h = []
    while stack:
        n, level = stack.pop()
        if level < len(h):
            n.next = h[level]
            h[level] = n
        else:
            h.append(n)
        if n.left:
            stack.append((n.left, level+1))
        if n.right:
            stack.append((n.right, level+1))

