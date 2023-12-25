"""
LC 134 : Gas Station

if rs[
There are `n` gas stations along a circular route, where the amount of gas at the ith station is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays `gas` and `cost`, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

Constraints:

    n == gas.length == cost.length
    1 <= n <= 105
    0 <= gas[i], cost[i] <= 104

"""
# 19 : 37
def start(gas, cost):
    starting_position = 0
    running_sum = 0
    total_gas = 0
    total_cost = 0
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        running_sum += gas[i] - cost[i]
        if running_sum < 0:
            running_sum = 0
            rv = i+1
    return -1 if total_sum < 0 else rv

# Using Kadane's algorithm (maximum subarray sum)
def start(gas, cost):
    n = len(gas)
    path = []
    indexes = []
    S = 0 # sum
    for i in range(n):
        e = gas[i]-cost[i]
        if e==0: continue
        path.append(e)
        indexes.append(i)
        S += e
    if not path: return 0
    if S < 0: return -1
    i, mxs = maxsum(path)
    j, mns = minsum(path)
    if mns < 0 and S-mns > mxs:
        return indexes[j+1]
    return indexes[i]

def maxsum(path):
    rs = path[-1] # running sum
    max_s = rs # max sum
    idx_s = len(path) - 1 # max sum index
    for i in range(len(path)-2, -1, -1):
        rs = max(rs+path[i], path[i])
        if max_s < rs:
            max_s = rs
            idx_s = i
    return idx_s, max_s

def minsum(path):
    rs = path[0] # running sum
    min_s = rs # min sum
    idx_s = 0 # min sum index
    for i in range(1, len(path)):
        rs = min(rs+path[i], path[i])
        if min_s >= rs:
            min_s = rs
            idx_s = i
    return idx_s, min_s

def start(gas, cost):
    starting_position = 0
    running_sum = 0
    total_gas = 0
    total_cost = 0
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        running_sum += gas[i] - cost[i]
        if running_sum < 0:
            running_sum = 0
            rv = i+1
    return -1 if total_gas - total_cost < 0 else rv

# same abbreviated
def start(gas, cost):
    # start index, running sum, sum gas, sum cost
    rv, rs, sg,  sc = 0, 0, 0, 0
    for i in range(len(gas)):
        sg += gas[i]
        sc += cost[i]
        rs += gas[i] - cost[i]
        if rs < 0:
            rs = 0
            rv = i+1
    return -1 if sg - sc < 0 else rv

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(start(gas, cost))
#Output: 3
gas = [2,3,4]
cost = [3,4,3]
print(start(gas, cost))
# Output: -1
gas = [5,8,2,8]
cost = [6,5,6,6]
print(start(gas, cost))
# Output: 3

"""
Insight: The key to the solution is to observe that intermediate values do not affect the outcome of picking the wrong starting position. Logically we can just skip all these intermediary values as our next candidates. The take away here is that there may be some hidden logical implications to watch out for about intermediary values, when a problem requires to select an earlier value while traversing those intermediaries and still reaching a particular state.
"""
