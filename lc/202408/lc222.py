# 35 - 42 (all solutions)
def count_nodes(root):
    def helper(node):
        if not node: return 0
        left = helper(node.left)
        right = helper(node.right)
        return left + right + 1
    return helper(root)

def count_nodes(root):
    res = [0]
    def helper(node):
        if not node: return
        res[0] += 1
        helper(node.left)
        helper(node.right)
    helper(root)
    return res[0]

# most efficient (100%)
def count_nodes(root):
    if not root: return 0
    res = 0
    stack = [root]
    while stack:
        res += len(stack)
        stack = [c for n in stack for c in (n.left, n.right) if c]
    return res
