def morris_preot(root):
    node = root
    while node:
        process(node)
        pre = morris_predecessor(node)
        if not pre:
            node = node.right
            continue
        if pre.right is node: 
            pre.right = None
            node = node.right
            continue
        pre.right = node
        node = node.left

def morris_iot(root):
    node = root
    while node:
        pre = morris_predecessor(node)
        if not pre:
            process(node)
            node = node.right
            continue
        if pre.right is node:
            pre.right = None
            process(node)
            node = node.right
            continue
        pre.right = node
        node = node.left

def morris_predecessor(node):
    pre = node.left
    if not pre: return
    while pre.right and pre.right is not node:
        pre = pre.right
    return pre
