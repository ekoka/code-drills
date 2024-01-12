"""
LC 199: Binary Tree Right Side View
"""

from collections import deque
from .bt import maketree
def solution1(root):
    q = deque()
    q.append(root)
    next_q = deque()
    rv = [root.val]
    while q:
        n = q.popleft()
        for child in (n.right, n.left):
            if not child: continue
            next_q.append(child)
        if not q:
            if not next_q:
                break
            rv.append(next_q[0].val)
            q = next_q
            next_q = deque()
    return rv

def rsv(node):
    if not node:
        return []
    res = []
    stack = [node]
    while stack:
        next_stack = []
        res.append(stack[0].val)
        for n in stack:
            if n.right:
                next_stack.append(n.right)
            if n.left:
                next_stack.append(n.left)
        stack = next_stack
    return res
                
def rsv(node):
    if not node:
        return []
    res = []
    stack = [node]
    while stack:
        next_stack = []
        res.append(stack[0].val)
        for n in stack:
            next_stack.append(n.right)
            next_stack.append(n.left)
        stack = list(filter(None, next_stack))
    return res


def rsv(node):
    res = []
    def hlp(n, lvl):
        if not n:
            return
        if lvl==len(res):
            res.append(n.val)
        hlp(n.right, lvl+1, res)
        hlp(n.left, lvl+1, res)
    hlp(node, 0)
    return res

def rsv_iter(node):                
    stack = [(node, 0)]
    res = []
    while stack:
        n, lvl = stack.pop()
        if not n:
            continue
        if lvl==len(res):
            res.append(n.val)
        stack.append((n.left, lvl+1))
        stack.append((n.right, lvl+1))
    return res

print(solution1(maketree([1,2,None,5])))
print(solution2(maketree([1,2,None,5])))
print(solution1(maketree([1,2,3,None,5,None,4])))
print(solution2(maketree([1,2,3,None,5,None,4])))
