"""
LC 120 : Triangle

Given a `triangle` array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

2
3 4
6 5 7
4 1 8 3
Example 2:

Input: triangle = [[-10]]
Output: -10

Constraints:

    1 <= triangle.length <= 200
    triangle[0].length == 1
    triangle[i].length == triangle[i - 1].length + 1
    -104 <= triangle[i][j] <= 104
 
Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""
# 29
def minpath(triangle):
    dp = [0]
    for row in triangle:
        new_dp = [0] * len(row)
        for i in range(len(row)):
            if i > 0 and i < len(dp):
                new_dp[i] = row[i] + (dp[i] if dp[i] <  dp[i-1] else dp[i-1])
            elif i < len(dp):
                new_dp[i] = row[i] + dp[i]
            elif i > 0:
                new_dp[i] = row[i] + dp[i-1]
        dp = new_dp
    return min(dp)

# bottom up (slower because of reverse range)
def minpath(triangle):
    dp = triangle[-1]
    for i in range(len(triangle)-2, -1, -1):
        new_dp = []
        for j in range(len(triangle[i])):
            new_dp.append(triangle[i][j] + (dp[j] if dp[j] < dp[j+1] else dp[j+1]))
        dp = new_dp
    return dp[0]

# more efficient, reuses same dp array
def minpath(triangle):
    triangle.reverse()
    dp = triangle[0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + (dp[j] if dp[j] < dp[j+1] else dp[j+1])
    return dp[0]

# same solution, but a bit more dp approved 
def minpath(triangle):
    triangle.reverse()
    dp = [0] * (len(triangle)+1) # len(triangle)==len(triange[-1])
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + (dp[j] if dp[j] < dp[j+1] else dp[j+1])
    return dp[0]

# slower because of reverse range
def minpath(triangle):
    dp = [0] * (len(triangle)+1)
    for i in range(len(triangle)-1, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + (dp[j] if dp[j] < dp[j+1] else dp[j+1])
    return dp[0]

# remember how height(triangle)==len(triangle[-1]), let's use that property
def minpath(triangle):
    dp = [0] * (len(triangle)+1)
    for i in range(len(triangle)-1, -1, -1):
        for j in range(i+1): # <-- 
            dp[j] = triangle[i][j] + (dp[j] if dp[j] < dp[j+1] else dp[j+1])
    return dp[0]
