"""
LC 210: Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]



Constraints:

    1 <= numCourses <= 2000
    0 <= prerequisites.length <= numCourses * (numCourses - 1)
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    ai != bi
    All the pairs [ai, bi] are distinct.
"""
# 56
def schedule(courses, prerequisites):
    rv = []
    graph = {c:[] for c in courses}
    for c, pre in prerequisites:
        graph[c].append(pre)
    for c in courses:
        if c not in graph:
            rv.append(c)
            continue
        if not dfs(graph, rv, c):
            return []
    return rv

def dfs(graph, acc, i):
    status, stack = {i:-1}, [i]
    while stack:
        c = stack[-1]
        if status[c]==1:
            stack.pop()
            continue
        if status[c]==0:
            status[c] = 1
            acc.append(c)
        if status[c]==-1:
            status[c] = 0
            for p in graph[c]:
                if status[p]==0:
                    return False
                if status[p]==-1:
                    stack.append(p)
    return True

def schedule(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    for c, p in prerequisites:
        graph[c].append(p)
    status = [0] * numCourses
    res = []
    def dfs(i):
        stack = [i]
        while stack:
            n = stack.pop()
            if status[n]==1:
                status[n] = 2
                res.append(n)
            elif status[n]==2: 
                continue
            else:
                stack.append(n)
                status[n] = 1 # discovered
                for c in graph[n]:
                    if status[c]==2: # processed
                        continue
                    if status[c]==1: # discovered
                        return False
                    stack.append(c)
        return True
    for i in range(numCourses):
        if status[i]==2: continue
        if not dfs(i):
            return []
    return res

def schedule(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    for c, p in prerequisites:
        graph[c].append(p)
    status = [0] * numCourses
    res = []
    for i in range(numCourses):
        if status[i]==2: continue
        stack = [i]
        while stack:
            n = stack.pop()
            if status[n]==1:
                status[n] = 2
                res.append(n)
            elif status[n]==2:
                continue
            else:
                stack.append(n)
                status[n] = 1 # discovered
                for c in graph[n]:
                    if status[c]==2: # processed
                        continue
                    if status[c]==1: # discovered
                        return []
                    stack.append(c)
    return res

