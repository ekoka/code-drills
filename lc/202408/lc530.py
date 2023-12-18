"""
LC 530: Minimum Absolute Difference in BST
"""
# 58
def mindiff(root):
    pre = [None]
    inf = float('inf')
    res = [inf]
    def helper(n):
        if not n: return
        helper(n.left)
        if pre[0] is not None:
            diff = n.val-pre[0]
            if res[0] > diff:
                res[0] = diff
        pre[0] = n.val
        helper(n.right)
    helper(root)
    if res[0]==inf: return 0
    return res[0]

def mindiff(root):
    stack = []
    pre = None
    res = float('inf')
    nxt = root
    while nxt:
        while nxt:
            stack.append(nxt)
            nxt = nxt.left
        while stack:
            n = stack.pop()
            if pre is not None:
                diff = n.val - pre
                if res > diff:
                    res = diff
            pre = n.val
            if n.right:
                nxt = n.right
                break
    return res


def mindiff(root):
    inf = float('inf')
    pre = -inf
    res = inf
    stack = [root]
    nxt = root.left
    while stack or nxt:
        if nxt:
            stack.append(nxt)
            nxt = nxt.left
            continue
        n = stack.pop()
        diff = n.val - pre
        if res > diff:
            res = diff
        pre = n.val
        nxt = n.right
    return res


