discovered = object()
processed = object()

def dfs(graph):
    for n in graph:
        if n.status is processed: continue
        process(n)

def process(node):
    node.status = discovered
    for c in node.children:
        if c.status is processed: continue
        if c.status is discovered:
            raise Exception('Cycle detected')
        process(c)
    node.status = processed

def process_iter(node):
    stack = [node]
    while stack:
        n = stack.pop()
        if n.status is processed: continue
        if n.status is discovered:
            process(n)
            n.status = processed
            continue
        n.status = discovered
        stack.append(n)
        for c in n.children:
            if c.status is discovered:
                raise Exception('Cycle detected')
            if c.status is processed:
                continue
            stack.append(c)

import collections
def bfs1(node):
    q = collections.deque()
    while q:
        n = q.popleft()
        process(n)
        n.status = processed
        for c in n.children:
            if c.status is processed: continue
            q.append(c)

def bfs2(node):
    q = []
    while q:
        nxt_q = []
        for n in q:
            process(n)
            n.status = processed
            for c in n.children:
                if c.status is processed: continue
                nxt_q.append(c)
        q = nxt_q
