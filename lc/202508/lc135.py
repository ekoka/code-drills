
"""
135. Candy

There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

Constraints:

    n == ratings.length
    1 <= n <= 2 * 104
    0 <= ratings[i] <= 2 * 104

"""
def candies(ratings):
    n = len(ratings)
    candies = [0] * n
    if n==1: return 1
    graph = rating_linearization(ratings)

    def dfs(i):
        if candies[i]: return
        res_i = 0
        for j in graph[i]:
            dfs(j)
            if res_i < candies[j]:
                res_i = candies[j]
        candies[i] = res_i + 1

    for i in range(n):
        if candies[i]: continue
        dfs(i)
    return sum(candies)
            
def rating_linearization(ratings):
    n = len(ratings)
    res = [[] for _ in ratings]
    # i depends on j
    for i in range(1, n):
        if ratings[i-1] < ratings[i]:
            res[i].append(i-1)
        elif ratings[i-1] > ratings[i]:
            res[i-1].append(i)
    return res

def candies(ratings):
    n = len(ratings)
    if n==1: return 1
    # i depends on j
    graph = [[None, None] for _ in ratings]
    for i in range(1, n):
        if ratings[i-1] < ratings[i]:
            graph[i][0] = i-1
        elif ratings[i-1] > ratings[i]:
            graph[i-1][1] = i

    candies = [0] * n
    def dfs(i):
        if i is None: return 0
        if candies[i]: return candies[i]
        left = dfs(graph[i][0])
        right = dfs(graph[i][1])
        candies[i] = 1 + (left if left > right else right)
        return candies[i]

    for i in range(n):
        if candies[i]: continue
        dfs(i)
    return sum(candies)

# greedy two passes
def candies(ratings):
    n = len(ratings)
    if n==1: return 1
    candies = [1] * n
    for i in range(1, n):
        if ratings[i-1] < ratings[i]:
            candies[i] = candies[i-1] + 1
    cnt = candies[n-1]
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
            candies[i] = candies[i+1] + 1
        cnt += candies[i]
    return cnt

ratings = [1,0,2]
exp = 5
res = candies(ratings)
print(res)
assert res==exp


ratings = [1,2,2]
exp = 4
res = candies(ratings)
print(res)
assert res==exp
