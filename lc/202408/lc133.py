"""
LC 133 : Clone Graph.

Constraints:
    The number of nodes in the graph is in the range [0, 100].
    1 <= Node.val <= 100
    Node.val is unique for each node.
    There are no repeated edges and no self-loops in the graph.
    The Graph is connected and all nodes can be visited starting from the given node.
"""
def clone(node):
    stack = [node]
    copies = {node.val: Node(node.val)}
    while stack:
        cur = stack.pop()
        cur_cpy = copies[cur.val]
        for nb in cur.neighbors:
            if nb.val not in copies:
                copies[nb.val] = Node(nb.val)
                stack.append(nb)
            cur_cpy.append(nb)
    return copies[node.val]

# better performance
def clone(node):
    if not node: return
    stack = [node]
    copies = {node.val: Node(node.val)}
    relationships = []
    while stack:
        n = stack.pop()
        for nb in n.neighbors:
            relationships.append((n.val, nb.val))
            if nb.val not in copies:
                copies[nb.val] = Node(nb.val)
                stack.append(nb)
    for a, b in relationships:
        copies[a].neighbors.append(copies[b])
    return copies[node.val]
