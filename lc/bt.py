import collections

class Node:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.left = l
        self.right = r
        self.next = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

def maketree(data):
    if not data:
        return
    q = collections.deque()
    i = 0
    makenode = lambda idx: None if data[idx] is None else Node(data[idx])
    root = makenode(i)
    q.append(root)
    while q:
        n = q.popleft()
        if n is None:
            continue
        try:
            n.left = makenode(i+1)
            n.right = makenode(i+2)
            q.append(n.left)
            q.append(n.right)
            i += 2
        except IndexError:
            break
    return root
