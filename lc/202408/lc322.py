"""
322. Coin Change

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Constraints:
    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 104
"""

def coin_change(coins, amount):
    rv = [-1] * (amount+1)
    rv[0] = 0
    coins.sort()
    for i in range(1, amount+1):
        for c in coins:
            if i-c < 0: break
            if rv[i-c]==-1: continue
            if rv[i]==-1 or rv[i-c] + 1 < rv[i]:
                rv[i] = rv[i-c] + 1
    return rv[-1]

def coin_change(coins, amount):
    if amount==0: return 0
    coins.sort()
    inf = float('inf')
    res = [inf] * (amount+1)
    for i in range(1, amount+1):
        for c in coins:
            if c > i: break
            if c==i:
                res[i] = 1
                break
            # if c < i
            if res[i-c] is inf: 
                continue 
            if res[i-c]+1 < res[i]:
                res[i] = res[i-c] + 1
    return -1 if res[-1] is inf else res[-1]
