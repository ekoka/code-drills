# 56 - 16
def has_pathsum(root, targetSum):
    def helper(n, target):
        if not n: return False
        if target==n.val:
            if not (n.left or n.right): 
                return True
        return helper(n.left, target-n.val) or helper(n.right, target-n.val)
    return helper(root, targetSum)

# efficient (100%)
def has_pathsum(root, targetSum):
    stack = [(root, targetSum)]
    while stack:
        n, t = stack.pop()
        if not n: continue
        if t==n.val:
            if not (n.left or n.right):
                return True
        nxt_t = t-n.val
        stack.append((n.left, nxt_t))
        stack.append((n.right, nxt_t))
    return False
