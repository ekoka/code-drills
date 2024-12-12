"""
LC 188. Best Time to Buy and Sell Stock IV

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Constraints:
    1 <= k <= 100
    1 <= prices.length <= 1000
    0 <= prices[i] <= 1000
"""

"""
requires to track:
- current low
- current sum
"""
def maxprofit(k, prices):
    n = len(prices)
    K = 2*k
    memo = [ [None] * (n+1) for _ in range(K+1) ]
    for j in range(n+1):
        memo[K][j] = 0
    for i in range(K+1):
        memo[i][n] = 0
    def helper(i, j, buysell_toggle):
        if memo[i][j] is not None: return memo[i][j]
        # process/ignore decision tree 
        processed = helper(i+1, j+1, -buysell_toggle)
        ignored = helper(i, j+1, buysell_toggle)
        amount = prices[j] * buysell_toggle
        memo[i][j] = max(processed + amount, ignored)
        return memo[i][j]
    return helper(0,0,-1)


def maxprofit(k, prices):
    n = len(prices)
    K = 2*k
    row = lambda: [{} for _ in range(n+1)] 
    memo = [ row() for _ in range(K+1) ]
    for j in range(n+1):
        memo[K][j] = {'buy': 0, 'sell': 0}
    for i in range(K+1):
        memo[i][n] = {'buy': 0, 'sell': 0}

    for i in range(K-1, -1, -1):
        for j in range(n-1, -1, -1):
            memo[i][j]['buy'] = max(memo[i+1][j+1]['sell'] - prices[j], memo[i][j+1]['buy'])
            memo[i][j]['sell'] = max(memo[i+1][j+1]['buy'] + prices[j], memo[i][j+1]['sell'])
    return memo[0][0]['buy']


k = 2
prices = [3,3,5,0,0,3,1,4]

#print(maxprofit(k, prices))

k = 2
prices = [6,1,3,2,4,7]
#print(maxprofit(k, prices))
"""
- grab i-1, j-1
- if previous price is lower, add the difference and record the sum. new low is current price.
- else (previous price is greater), nothing to add, current price becomes new low.
"""
# opnum : number of operation
def solve(index, opnum, k, prices):
    if index==len(prices):
        return 0
    if opnum==2*k:
        return 0
    profit = 0
    if opnum % 2:
        # sell allowed
        sellkaro = solve(index+1, opnum+1, k, prices) + prices[index]
        ignorekaro = solve(index+1, opnum, k, prices) + 0
        profit = max(sellkaro, ignorekaro)
    else:
        # buy allowed
        buykaro = solve(index+1, opnum+1, k, prices) - prices[index]
        skipkaro = solve(index+1, opnum, k, prices) + 0
        profit = max(buykaro, skipkaro)
    return profit
    
def solve(index, opnum, k, prices):
    if index==len(prices):
        return 0
    if opnum==2*k:
        return 0
    sell = opnum % 2
    profit = 0
    res = solve(index+1, opnum+1, k, prices)
    skip = solve(index+1, opnum, k, prices) # ignore current price
    return max(res + prices[index] * (1 if opnum%2 else -1), skip)
 
def maxProfit(k, prices):
     return solve(0, 0, k, prices)

def maxprofit(k, prices):
    n = len(prices)
    # for k=1
    total_max_after_purchase = [ [-prices[0]] * n for _ in range(k) ]
    total_max_after_sale = [ [0] * n for _ in range(k) ]
    for j in range(1, n):
        total_max_after_sale[0][j] = max(total_max_after_purchase[0][j-1] + prices[j], total_max_after_sale[0][j-1])
        total_max_after_purchase[0][j] = max(-prices[j], total_max_after_purchase[0][j-1])
    # for k > 1 
    for i in range(1, k):
        for j in range(1, n):
            total_max_after_sale[i][j] = max(total_max_after_purchase[i][j-1] + prices[j], total_max_after_sale[i][j-1])
            total_max_after_purchase[i][j] = max(total_max_after_sale[i-1][j-1] - prices[j], total_max_after_purchase[i][j-1])
    return total_max_after_sale[-1][-1]

def maxprofit(k, prices):
    n = len(prices)
    # for k=1
    total_max_after_purchase = [ [-prices[0]] * n for _ in range(k) ]
    total_max_after_sale = [ [0] * n for _ in range(k) ]
    for j in range(1, n):
        total_max_after_sale[0][j] = max(total_max_after_purchase[0][j-1] + prices[j], total_max_after_sale[0][j-1])
        total_max_after_purchase[0][j] = max(-prices[j], total_max_after_purchase[0][j-1])
    # for k > 1 
    for i in range(1, k):
        for j in range(1, n):
            total_max_after_sale[i][j] = max(total_max_after_purchase[i][j-1] + prices[j], total_max_after_sale[i][j-1])
            total_max_after_purchase[i][j] = max(total_max_after_sale[i-1][j-1] - prices[j], total_max_after_purchase[i][j-1])
    return total_max_after_sale[-1][-1]

def maxprofit(k, prices):
    n = len(prices)
    pre = [0] * n 
    cur = [0] * n
    for i in range(k):
        total_max_after_purchase = -prices[0]
        for j in range(1, n):
            cur[j] = max(total_max_after_purchase + prices[j], cur[j-1])
            total_max_after_purchase = max(pre[j-1] - prices[j], total_max_after_purchase)
        pre, cur = cur, pre
    return pre[-1]

def maxprofit(k, prices):
    n = len(prices)
    cur = [0] * n
    for i in range(k):
        total_max_after_purchase = -prices[0]
        tmpmax = 0
        for j in range(1, n):
            nxt_tmpmax = cur[j]
            if total_max_after_purchase + prices[j] > cur[j-1]:
                cur[j] = total_max_after_purchase + prices[j]
            else:
                cur[j] = cur[j-1]
            if tmpmax - prices[j] > total_max_after_purchase:
                total_max_after_purchase = tmpmax - prices[j]
            tmpmax = nxt_tmpmax
    return cur[-1]

## Test
k = 2
prices = [2,4,1]
expected = 2
output = maxprofit(k, prices)
print(output)
print(output is expected)

k = 2
prices = [3,2,6,5,0,3]
expected = 7
output = maxprofit(k, prices)
print(output)
print(output is expected)

k = 2
prices = [6,1,3,2,4,7]
expected = 7
output = maxprofit(k, prices)
print(output)
print(output is expected)

k = 2
prices = [3,3,5,0,0,3,1,4]
expected = 6
output = maxprofit(k, prices)
print(output)
print(output is expected)

k = 2
prices = [2,1,4,5,2,9,7]
expected = 11
output = maxprofit(k, prices)
print(output)
print(output is expected)
