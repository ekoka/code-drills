# 11 - 25 (100%)
def is_same_tree(p, q):
    stack = [(p, q)]
    while stack: 
        nxt_stack = []
        for a, b in stack:
            if (not a) or (not b):
                if a!=b: return False
                continue
            if a.val!=b.val: return False
            nxt_stack.extend((x,y) for x,y in ((a.left, b.left), (a.right, b.right)))
        stack = nxt_stack
    return True
