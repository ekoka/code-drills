def longest_common_prefix(strs):
    n = len(strs)
    m = 200 
    for s in strs:
        if len(s) < m:
            m = len(s)
    for i in range(m):
        for j in range(n):
            if strs[j-1][i]!=strs[j][i]:
                return strs[0][0:i]
    return strs[0][0:m]


