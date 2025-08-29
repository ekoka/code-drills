def start(gas, cost):
    n = len(gas)
    s = 0
    S = 0
    res = None
    for i in range(n):
        v = gas[i] - cost[i]
        S += v
        s += v
        if s < 0:
            s = 0
            res = -1
        elif res == -1:
            res = i
    if S < 0:
        return -1
    return res


def start(gas, cost):
    if sum(gas) - sum(cost) < 0:
        return -1
    s = 0
    res = -1
    for i in range(len(gas)):
        s += gas[i] - cost[i]
        if s < 0:
            res = -1
            s = 0
        elif res==-1: 
            res = i
    return res
