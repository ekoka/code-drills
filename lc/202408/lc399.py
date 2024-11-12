"""
LC 399: Evaluate Division

You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation `Ai / Bi = values[i]`. Each `Ai` or `Bi` is a string that represents a single variable.

You are also given some queries, where `queries[j] = [Cj, Dj]` represents the jth query where you must find the answer for `Cj / Dj = ?`.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:

    1 <= equations.length <= 20
    equations[i].length == 2
    1 <= Ai.length, Bi.length <= 5
    values.length == equations.length
    0.0 < values[i] <= 20.0
    1 <= queries.length <= 20
    queries[i].length == 2
    1 <= Cj.length, Dj.length <= 5
    Ai, Bi, Cj, Dj consist of lower case English letters and digits.


## Insights
1. Observe how a relationship can be described with separate data structures.
2. Some relationships in a graph may infer new ones. For instance, the distance from A to B and from B to C, may infer at least one possible distance from A to C.
"""
# 12
def solution(equations, values, queries):
    rv, graph = [], {}
    for e,v in zip(equations, values):
        graph.setdefault(e[0], {})[e[1]] = v
        graph.setdefault(e[1], {})[e[0]] = 1/v
    for x, y in queries:
        if x in graph and y in graph:
            #rv.append(dfs(graph, x, y))
            rv.append(bfs(graph, x, y))
        else:
            rv.append(-1.0)
    return rv

def bfs(graph, x, y):
    graph[x][x] = 1.0
    visited, stack = set(), [x]
    while stack:
        new_stack = []
        for a in stack:
            visited.add(a)
            if a==y:
                return graph[x][a]
            for b in graph[a]:
                if b in visited: continue
                graph[x][b] = graph[x][a] * graph[a][b] # x to b
                graph[b][x] = 1/graph[x][b]
                new_stack.append(b)
        stack = new_stack
    return -1.0

def solution(equations, values, queries):
    graph = {}
    for i in range(len(equations)):
        x, y = equations[i]
        graph.setdefault(x, {})[y] = values[i]
        graph.setdefault(y, {})[x] = 1/graph[x][y]
    res = []
    for x,y in queries:
        res.append(bfs(graph, x,y))
    return res

def bfs(graph, x, y):
    if x not in graph: return -1.0
    if y not in graph: return -1.0
    graph[x][x] = 1.0
    stack = [x]
    discovered = {x}
    while stack:
        next_stack = []
        while stack:
            n =  stack.pop()
            if n==y: return graph[x][y]
            for c in graph[n]:
                if c in discovered: continue
                discovered.add(c)
                graph[x][c] = graph[x][n] * graph[n][c]
                graph[c][x] = 1/graph[x][c]
                next_stack.append(c)
        stack = next_stack
    return -1.0

def solution(equations, values, queries):
    graph = {}
    res = []
    def bfs(x, y):
        if not (x in graph and y in graph): return -1.0
        graph[x][x] = 1.0
        stack = [x]
        discovered = {x}
        while stack:
            next_stack = []
            while stack:
                n =  stack.pop()
                if n==y: return graph[x][y]
                for c in graph[n]:
                    if c in discovered: continue
                    discovered.add(c)
                    graph[x][c] = graph[x][n] * graph[n][c]
                    graph[c][x] = 1/graph[x][c]
                    next_stack.append(c)
            stack = next_stack
        return -1.0
    for i in range(len(equations)):
        x, y = equations[i]
        graph.setdefault(x, {})[y] = values[i]
        graph.setdefault(y, {})[x] = 1/graph[x][y]
    for x,y in queries:
        res.append(bfs(graph, x,y))
    return res

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
rv = solution(equations, values, queries)
print(rv)
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
assert rv == [6.00000,0.50000,-1.00000,1.00000,-1.00000]

equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
rv = solution(equations, values, queries)
print(rv)
assert rv == [3.75000,0.40000,5.00000,0.20000]
# Output: [3.75000,0.40000,5.00000,0.20000]

equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
rv = solution(equations, values, queries)
print(rv)
assert rv == [0.50000,2.00000,-1.00000,-1.00000]
#Output: [0.50000,2.00000,-1.00000,-1.00000]
