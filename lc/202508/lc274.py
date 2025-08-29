def h_index(citations):
    citations.sort()
    n = len(citations)
    h = 0
    for i in range(n):
        if n-i < h and n-i <= citations[i]:
            h = n-i
    return h

