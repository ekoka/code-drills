def preot(node, acc):
    proces(node, acc)
    preot(node.left, acc)
    preot(node.right, acc)

def postot(node): 
    left = postot(node.left)
    right = postot(node.right)
    process(node, left, right)

def iot(node):
    iot(node.left)
    process(node)
    iot(node.right)

def lot(node):
    q = collection.deque([node])
    while q:
        n = q.popleft()
        if not n: continue
        process(n)
        q.append(n.left)
        q.append(n.right)

def iot2(node):
    q = []
    while q:
        nxt_q = []
        while q:
            n = q.pop()
            if not n: continue
            process(n)
            nxt_q.append(n.right)
            nxt_q.append(n.left)
        q = nxt_q

def preot_it(node):
    stack = [node]
    while stack:
        n = stack.pop()
        process(n)
        stack.append(n.right)
        stack.append(n.left)

def iot_it1(node):
    stack = [node]
    nxt = stack.left
    while stack or nxt:
        if nxt:
            stack.append(nxt)
            nxt = nxt.left
            continue
        n = stack.pop()
        process(n)
        nxt = n.right

def iot_it2(node):
    stack = [node]
    nxt = stack.left
    while stack:
        while nxt:
            stack.append(nxt)
            nxt = nxt.left
        while not nxt and stack:
            n = stack.pop()
            process(n)
            nxt = n.right

def postot1(node):
    stack = preot_stack(node)
    result = []
    while stack:
        n = stack.pop()
        if n is None:
            result.append(None)
            continue
        left = result.pop()
        right = result.pop()
        result.append(process(n, left, right))
    return result[0]

def preot_stack(node):
    iter_stack = [node]
    result_stack = []
    while iter_stack:
        n = iter_stack.pop()
        result_stack.append(n)
        if n is None: continue
        iter_stack.append(n.right)
        iter_stack.append(n.left)
    return result_stack
        
def postot2(node):
    discovered = True
    stack = [(node, not discovered)]
    result = []
    while stack:
        n, is_discovered = stack.pop()
        if n is None:
            result.append(None)
        elif is_discovered:
            right = result.pop()
            left = result.pop()
            result.append(process(n, left, right))
        else: # is not discovered:
            stack.append((n, discovered))
            stack.append((n.right, not discovered))
            stack.append((n.left, not discovered))
    return result[0]
