"""
LC 103: Binary Tree Zigzag Level Order Traversal
"""

from .bt import maketree

def solution1(root):
    if not root:
        return []
    zig = True
    rv = []
    stack = [root]
    while stack:
        level = []
        current_stack = stack
        stack = []
        while current_stack:
            n = current_stack.pop()
            level.append(n.val)
            children = (n.left, n.right) if zig else (n.right, n.left)
            for c in children:
                if c is None: continue
                stack.append(c)
        rv.append(level)
        zig = not zig
    return rv

def zigzaglo(node):
    res = []
    stack = [node]
    while stack:
        new_stack = []
        lvl_res = []
        while stack:
            n = stack.pop()
            if not n:
                continue
            lvl_res.append(n)
            if len(res) % 2:
                new_stack.append(n.right)
                new_stack.append(n.left)
            else:
                new_stack.append(n.left)
                new_stack.append(n.right)
        stack = new_stack
        res.append(lvl_res)
    res.pop()
    return res

def zigzaglo(root):
    stack = [root]
    res = []
    reverse = False
    while stack:
        nxt_stack = []
        level = []
        while stack:
            n = stack.pop()
            level.append(n.val)
            c1, c2 = n.right, n.left if reverse else n.left, n.right
            if c1:
                nxt_stack.append(c1)
            if c2:
                nxt_stack.append(c2)
        reverse = !reverse
        res.append(level)
        stack = nxt_stack
    return res

print(solution1(maketree([3,9,20,None,None,15,7])))
print(solution1(maketree([1])))
print(solution1([]))
