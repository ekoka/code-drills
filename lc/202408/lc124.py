"""
LC 124 : Binary Tree Maximum Path Sum
"""
# 27 - 48
def max_path_sum(root):
    res = [float('-inf')]
    def helper(node):
        if node is None: return 0
        left = helper(node.left)
        right = helper(node.right)
        local_sum = left+right+node.val
        if local_sum > res[0]:
            res[0] = local_sum
        rv = max(node.val, left+node.val, right+node.val)
        if rv > res[0]:
            res[0] = rv
        return rv
    helper(root)
    return res[0]

def max_path_sum(root):
    stack = [(root, False)]
    max_sum = float('-inf')
    memo = []
    while stack:
        n, processing = stack.pop()
        if not n: 
            memo.append(0)
            continue
        if processing:
            left = memo.pop()
            right = memo.pop()
            local_s = left+right+n.val
            if left==0 or right==0:
                s = local_s
            else:
                s = max(left, right) + n.val
                if local_s > max_sum:
                    max_sum = local_s
            if s > max_sum:
                max_sum = s
            if s < 0:
                memo.append(0)
            else:
                memo.append(s)
        else:
            stack.append((n, True))
            stack.append((n.left, False))
            stack.append((n.right, False))
    return max_sum


def max_path_sum(root):
    stack = [(root, False)]
    max_sum = float('-inf')
    memo = []
    while stack:
        n, processing = stack.pop()
        if n is None: 
            memo.append(0)
            continue
        if processing:
            left = memo.pop()
            right = memo.pop()
            lo, hi = (left, right) if left < right else (right, left)
            s = n.val + hi
            if s > max_sum:
                max_sum = s
            memo.append(0 if s<0 else s)
            if lo:
                s += lo
                if s>max_sum:
                    max_sum = s
        else:
            stack.append((n, True))
            stack.append((n.left, False))
            stack.append((n.right, False))
    return max_sum
