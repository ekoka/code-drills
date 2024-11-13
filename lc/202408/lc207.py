"""
LC 207: Course Schedule

There are a total of `numCourses` courses you have to take, labeled from 0 to numCourses - 1. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:

    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.

"""
# 44
def solution(courses, prerequisites):
    #graph = {c:[] for c,p in prerequisites}
    graph = {}
    for a,b in prerequisites:
        graph.setdefault(a,[]).append(b)
        #graph[a].append(b)
    #for i in tuple(graph.keys()):
    for i in range(courses):
        if i not in graph: continue
        if not dfs(graph, i):
            return False
        if not graph: break
    return True

#def dfs(graph, i, visited=None):
#    if visited is None:
#        visited = {i}
#    for c in graph[i]:
#        if c in visited:
#            return False
#        if c in graph:
#            if not dfs(graph, visited, c):
#                return False
#    del graph[i]
#    visited.remove(i)
#    return True


def dfs(graph, i):
    visited, stack = set(), [i]
    while stack:
        n = stack[-1]
        if n not in graph:
            stack.pop()
            continue
        if n in visited:
            stack.pop()
            del graph[n]
            visited.remove(n)
            continue
        visited.add(n)
        for c in graph[n]:
            if c in visited:
                return False
            if c in graph:
                stack.append(c)
    return True

def solution(numCourses, prerequisites): # efficient
    graph = [ [] for _ in range(numCourses) ]
    deps = [0] * numCourses
    for i,j in prerequisites:
        deps[i] += 1
        graph[j].append(i)
    stack = [i for i in range(numCourses) if deps[i]==0]
    res = 0
    while stack:
        i = stack.pop()
        res += 1
        for c in graph[i]:
            deps[c] -= 1
            if deps[c]==0:
                stack.append(c)
    return res==numCourses

print(solution(2, [[1,0]]))
print(solution(2, [[1,0], [0,1]]))
print(solution(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]))
print(solution(7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]))
