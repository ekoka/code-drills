# 57
class TreeNode:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.left = l
        self.right = r

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

def build(inorder, postorder):
    N = len(postorder)
    index_of_val = {v:i for i,v in enumerate(inorder)}
    def helper(i,j,k):
        if j==k: return
        n = TreeNode(postorder[i])
        idx = index_of_val[n.val]
        if idx==k:
            n.left = helper(i-1, j, k-1)
        else:
            sz = k+1 - (idx+1)
            n.right = helper(i-1, idx+1, k)
            n.left = helper(i-1 - sz, j, idx)
        return n 
    return helper(N-1, 0, N)

            
def build(inorder, postorder):
    N = len(postorder)
    index_of_val = {v:i for i,v in enumerate(inorder)}
    preroot = TreeNode()
    stack = [(N-1, 0, N, preroot, True)] # i, j, k, parent, left/right
    while stack:
        i, j, k, parent, right = stack.pop()
        if j==k: continue
        n = TreeNode(postorder[i])
        if right:
            parent.right = n
        else:
            parent.left = n
        idx = index_of_val[n.val]
        if idx==k:
            stack.append((i-1, j, k-1, n, False))
        else:
            sz = k+1 - (idx+1)
            stack.append((i-1, idx+1, k, n, True))
            stack.append((i-1 - sz, j, idx, n, False))
    return preroot.right

# changing from postorder to preorder (with right visited first)
def build(inorder, postorder):
    N = len(postorder) # but right visited first
    preorder = list(reversed(postorder))
    index_of_val = {v:i for i,v in enumerate(inorder)}
    preroot = TreeNode()
    stack = [(0, 0, N, preroot, True)] # i, j, k, parent, left/right
    while stack:
        i, j, k, parent, right = stack.pop()
        if j==k: continue
        n = TreeNode(preorder[i])
        if right:
            parent.right = n
        else:
            parent.left = n
        idx = index_of_val[n.val]
        if idx==k:
            stack.append((i-1, j, k-1, n, False))
        else:
            stack.append((i+k-idx, j, idx, n, False)) # left
            stack.append((i+1, idx+1, k, n, True)) # right 
    return preroot.right

# Tests

import collections
def printlot(root, acc=None):
    res = []
    q = collections.deque([root])
    while q:
        n = q.popleft()
        res.append(n.val if n else None)
        if not n: continue
        q.append(n.left)
        q.append(n.right)
    return res

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
root = build(inorder, postorder)
print(printlot(root))
#Output: [3,9,20,null,null,15,7]

inorder = [-1]
postorder = [-1]
root = build(inorder, postorder)
print(printlot(root))
# Output: [-1]
