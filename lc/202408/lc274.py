"""
LC 274 : H-Index

Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:

Input: citations = [1,3,1]
Output: 1

Constraints:

    n == citations.length
    1 <= n <= 5000
    0 <= citations[i] <= 1000

"""
# 52 - 8
def h_index(citations):
    N = len(citations)
    citations.sort()
    h = 0
    for i in range(N):
        if N-i >= citations[i]:
            return citations[i]
        c = min(N-i, citations[i])
        if rv < c:
            rv = c
    return rv

def h_index(citations):
    N = len(citations)
    citations.sort()
    h = 0
    for i in range(N):
        if N-i <= citations[i]:
            h = max(h, N-i)
    return h

citations = [3,0,6,1,5]
print(h_index(citations))
# Output: 3
citations = [6,3,0,6,1,5,4,4,5,7]
# [0,1,3,4,4,5,5,6,6,7]
print(h_index(citations))
# Output 5
citations = [1,3,1]
print(h_index(citations))
# Output 1
citations = [1,3,1,2]
print(h_index(citations))
# Output 2
citations = [100]
print(h_index(citations))
# Output 1
citations = [11,12]
print(h_index(citations))
# Output 2
