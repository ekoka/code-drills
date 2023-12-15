# 59 - 06 (100%)
def maxdepth(root):
    def helper(node)
        if node is None: return 0
        left = helper(node.left)
        right = helper(node.right)
        return max(left, right) + 1
    return helper(root)

def maxdepth(root):
    if not root: return 0
    depth = 0
    stack = [root]
    while stack:
        nxt_stack = []
        for n in stack:
            nxt_stack.extend(c for c in (n.left, n.right) if c) 
        stack = nxt_stack
        depth += 1
    return depth


