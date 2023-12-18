# 11 - 16 - 25
def average_of_levels(root):
    stack = [root]
    res = []
    while stack:
        res.append(sum(stack)/len(stack))
        stack = [c for n in stack for c in (n.left, n.right) if c]
    return res

# more performant (less syntax sugar)
def average_of_levels(root):
    stack = [root]
    res = []
    while stack:
        nxt_stack = []
        s = 0
        for n in stack:
            s += n.val
            if n.left:
              nxt_stack.append(n.left)
            if n.right:
              nxt_stack.append(n.right)
        res.append(s/len(stack))
        stack = nxt_stack
    return res
