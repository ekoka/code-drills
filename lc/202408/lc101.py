# 39 - 55
def is_symmetric(root):
    stack = [root]
    while stack:
        row = []
        for i in range(len(stack)//2):
            n1 = stack[i]
            n2 = stack[-1-i]
            if n1 is None or n2 is None:
                if n1 or n2:
                    return False
                continue
            if n1.val!=n2.val:
                return False
        nxt_stack = []
        for n in stack: 
            if not n: continue  
            for c in (n.left, n.right):
                nxt_stack.append(c)
        stack = nxt_stack
    return True
         
