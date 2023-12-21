"""
LC 108: Convert Sorted Array to Binary Tree.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBst(nums):
    def helper(start, stop):
        if start==stop: return
        m = (start+stop)//2
        return TreeNode(
            nums[m], 
            helper(start, m),   # left
            helper(m+1, stop),  # right 
        )
    return helper(0, len(nums))
    
def sortedArrayToBst(nums):
    start = [0]
    stop = [len(nums)]
    postorder = [False]
    res = []
    while start:
        st = start.pop()
        sp = stop.pop()
        if postorder.pop():
            res.append(TreeNode(nums[st], left=res.pop(), right=res.pop()))
            continue
        if st>=sp:
            res.append(None)
            continue

        postorder.append(True)
        m = (st+sp)//2
        start.append(m)
        stop.append(None)

        postorder.append(False)
        postorder.append(False)
        start.append(st)
        stop.append(m)
        start.append(m+1)
        stop.append(sp)
    return res[0]

def sortedArrayToBst(nums)
    stack = preot_stack(nums)
    res = []
    while stack:
        n = stack.pop()
        if not n:
            res.append(None)
            continue
        n.left = res.pop()
        n.right = res.pop()
        res.append(n)
    return res[0]

def preot_stack(nums):
    start = [0]
    stop = [len(nums)]
    res = []
    while start:
        st = start.pop()
        sp = stop.pop()
        if st>=sp:
            res.append(None)
            continue
        m = (st+sp)//2
        res.append(TreeNode(nums[m]))
        start.append(m+1)
        stop.append(sp)
        start.append(st)
        stop.append(m)
    return res



