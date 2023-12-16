# 27 - 38 (100%)
def invert_tree(root):
    def helper(root):
        if not root: return
        helper(root.left)
        helper(root.right)
        root.left, root.right = root.right, root.left
    return helper(root)

def invert_tree(root):
    if not root: return
    stack = [root]
    while stack:
        for n in stack:
            n.left, n.right = n.right, n.left 
        stack = [c for n in stack for c in (n.left, n.right) if c]
    return root
