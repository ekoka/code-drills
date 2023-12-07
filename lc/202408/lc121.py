"""
LC 121 : Best time to buy and sell stocks.
"""
# 53 - 23
def max_profit(prices):
    running_min = prices[0]
    running_max = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > running_max:
            running_max = prices[i]
            if running_max - running_min > profit:
                profit = running_max - running_min
        if prices[i] < running_min:
            running_min = prices[i]
            running_max = prices[i]
    return profit

def max_profit(prices): # derived from dp
    running_min = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] < running_min:
            running_min = prices[i]
        else:
            if prices[i] - running_min > profit:
                profit = prices[i] - running_min
    return profit
