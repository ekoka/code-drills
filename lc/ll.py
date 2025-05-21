class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        l = self
        rv = []
        while l:
            rv.append(l.val)
            l = l.next
        return f'{rv}'

def makelist(values):
    head = L = Node(values[0])
    for i,v in enumerate(values):
        if i==0: continue
        L.next = Node(v)
        L = L.next
    return head
