"""
LC 123: Best Time to Buy and Sell Stock III 

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:
    1 <= prices.length <= 105
    0 <= prices[i] <= 105

- The maximum local profit at any given selling point is the price at that point minus the price at the lowest previous point.
- If we select this selling point, we can't reuse any of its previous points.

- the maximum overall profit at any given selling point is the sum of :
    - the previous largest difference.
    - the largest difference between then and now.

- if that maximum overall profit is greater than the recorded one, it's recorded in its stead. 

- When a new largest difference is recorded, its selling point is recorded as the starting point for the discovery subsequent differences (or stopping po.

"""
def maxprofit(prices):
    maxp = 0
    lowest = prices[0]
    profits = [0] * len(prices)
    for i in range(1, n):
        if prices[i] < lowest:
            lowest = prices[i]
        if prices[i] - lowest > maxp:
            maxp = prices[i] - lowest
        profits[i] = maxp

    maxp = 0
    highest = prices[-1]
    res = profits[-1]
    for j in range(n-2, -1, -1):
        if prices[j] > highest:
            highest = prices[j]
        if highest - prices[j] > maxp:
            maxp = highest - prices[j]
        p = profits[j] + maxp 
        if p > res:
            res = p
    return res


def maxprofit(prices):
    if len(prices)==1: return 0
    f = forward(prices)
    b = backward(prices)
    return f if f > b else b 

def forward(prices):
    n = len(prices)
    res = 0
    lowest_buying_price = prices[0]
    running_buying_price = prices[0]
    best_sale = 0

    for sell_index in range(1, n):
        current_price = prices[sell_index]
        if current_price < running_buying_price:
            running_buying_price = current_price 
            if current_price < lowest_buying_price:
                lowest_buying_price = current_price
            continue

        current_total = best_sale + (current_price-running_buying_price)
        if current_total > res:
            res = current_total

        current_best_sale = current_price - lowest_buying_price
        if current_best_sale > best_sale:
            best_sale = current_best_sale 
            running_buying_price = current_price # reset running buying price
    return res

def forward(prices):
    res = 0
    inf = float('inf')
    lowest_buying_price = inf
    running_buying_price = inf
    best_sale = 0
    for current_price in prices:
        if current_price < running_buying_price:            # cond 1
            running_buying_price = current_price 
        if current_price < lowest_buying_price: # will also be run on cond 1 
            lowest_buying_price = current_price
        # if current_price < running_buying_price => False (will be skipped on cond 1)
        if res < best_sale + (current_price-running_buying_price):
            res = best_sale + (current_price-running_buying_price)

        # if current_price < running_buying_price => False
        if best_sale < current_price - lowest_buying_price:
            best_sale = current_price - lowest_buying_price:
            #running_buying_price = current_price #  not necessary
    return res

def forward(prices):
    res = 0
    inf = float('inf')
    lowest_buying_price = inf
    running_buying_price = inf
    best_sale = 0
    for current_price in prices:
        res = max(res, best_sale + (current_price-running_buying_price))
        lowest_buying_price = min(current_price, lowest_buying_price)  
        best_sale = max(best_sale, current_price - lowest_buying_price)
        running_buying_price = min(running_buying_price, current_price) 
    return res

def backward(prices):
    n = len(prices)
    res = 0
    absolute_highest_selling_price = prices[-1]
    current_highest_selling_price = prices[-1]
    current_highest_difference = 0

    for buy_index in range(n-2, -1, -1):
        current_price = prices[buy_index]
        if current_price > current_highest_selling_price:
            current_highest_selling_price = current_price 
            if current_price > absolute_highest_selling_price:
                absolute_highest_selling_price = current_price
            continue

        current_total = current_highest_difference + (current_highest_selling_price-current_price)
        if current_total > res:
            res = current_total

        diff = absolute_highest_selling_price-current_price
        if diff > current_highest_difference:
            current_highest_difference = diff 
            current_highest_selling_price = current_price
    return res


    def maxProfit(self, prices: List[int]) -> int:
        buy1 = float('inf')
        profit1 = 0
        buy2 = float('inf')
        profit2 = 0

        for price in prices:
            if buy1 > price:
                buy1 = price

            if profit1 < price-buy1:
                profit1 = price - buy1

            if buy2 > price - profit1:
                buy2 = price - profit1

            if profit2 < price - buy2:
                profit2 = price - buy2

        return profit2

def forward(prices):
    lowest_buying_price = float('inf')
    running_buying_price = float('inf')
    best_sale = 0
    res = 0
    for current_price in prices:
        res = max(res, best_sale + (current_price-running_buying_price))
        lowest_buying_price = min(current_price, lowest_buying_price)  
        best_sale = max(best_sale, current_price - lowest_buying_price)
        running_buying_price = min(running_buying_price, current_price) 
    return res

def forward(prices):
    buy1 = buy2 = float('inf')
    sell1 = sell2 = 0
    for p in prices:
        sell2 = max(sell2, sell1 + (p-buy2))
        buy1 = min(p, buy1)  
        sell1 = max(sell1, p - buy1)
        buy2 = min(buy2, p) 
    return sell2

def maxProfit(prices: List[int]) -> int:
    buy1 = buy2 = float('-inf')
    sell1 = sell2 = 0
    for p in prices:
        buy1 = max(buy1, -p)
        sell1 = max(sell1, buy1 + p)
        buy2 = max(buy2, sell1 - p)
        sell2 = max(sell2, buy2 + p)
    return sell2
"""
My remark about this problem:
    - to solve this kind of problem it's really helpful to have a fair number and variety of test cases. It's very easy to get false positives and for wrong assumptions to creep into the solution. You need many tests to cover all corner cases.
    - the difficulty in the problem is to expose the right level of abstraction that in turn exposes a clear path to a solution. Only once the abstraction is made more obvious that can the CS theory become useful. In other words, the real difficulty in this problem is to figure out what the problem really is logically.

    Although a strong candidates familiar enough with dynamic programming techniques would not be troubled by this aspect, they might find that they have a more difficult time in figuring out the relationship between stock prices in the timeline and how the limit of two transactions affects the outcome. In other words, what exactly does maximizing the profit in only two transactions imply logically. If the solver can work this out, which involves almost no programming thinking, they're probably 80% on their way to the soltution.
    - Because of this, I don't think this is such a good problem to solve in an interview setting.
    - This would be an excellent take-home problem, if the company is looking for a particularly strong coder *and* logical thinker. But the difficulty may incite a number of candidates to cheat. You'd need to probe that they at least understand the solution they presented you.
    - Although the problem is classified as dynamic programming, I didn't perceive that thinking in terms of tabulation was particularly helpful. It could be a side-effect of having already done a fair amount of dp problems, but I thought the ability to rather think in terms of "running values" was more helpful to me. Incidentally, it produced a more time-efficient solution than the vast majority (>97% on Leetcode).

Lessons learned:
    - most dp problems should produce the same result going forward than going backward. This wasn't the case here. So it might be useful to test that the logic that encapsulates the solution is valid both ways.


Problem solution
- When the problem is presented, we're told that we're limited to only two transactions and that want to maximize our profits in those two transactions.

- What does that actually mean in logical terms that can be translated into a program?

- Let's break this down until we get to a different description of the problem that can translate into something that matches something we know from CS theory. That is, let's redefine the problem until it resembles a familiar algorithm or resolution technique that can lead to the answer.

- To do this, I'll just do a brain dump of various facts or properties.

- There's a limit of 2 transactions.
- A transaction is made up of a purchase and a sale.
- maximizing the profit implies that I must select the two largest transactions or the two most profitable buying and selling combinations.
- The maximum profit we can have at any given day on a timeline is the price on that day minus the single lowest previous price on the timeline.

    timeline = [ a b c d e f g ] 
    profit[e] = price[e] - min(price[a], price[b], price[c], price[d])

- or assuming that we're tracking the minimum price,

    profit[e] = price[e] - min_price

- Thus at any given point D on the timeline between days X and Y, the overall maximum possible profit is the largest possible such difference from X up to and including D.

    timeline = [ a b c d e f g ] 
    max_profit[d] = max(profit[a], profit[b], profit[c], profit[d])

- or assuming we're tracking and recording this information as we're traversing the timeline,

    max_profit[d] = highest(max_profit[d-1], profit[d])

- Now, notice that picking a sell date as a transaction date invalidates all previous dates as possible buy dates for subsequent possible transactions. So we can already redefine the problem statement as "picking the two mutually compatible transactions that sum up to the highest amount".
- If we pick a selling point on the timeline all buying points before it are now unavailable for the next transactions.
- If we thus visualize the timeline, picking the two best possible compatible transactions means finding a point x on the timeline such that on either side of x we can find transactions A and B that together, add up to the most profitable sum.

    | ... A ... x ... B ... |

- This reframes the problem into something that already offers glimpses of being simpler to work out programmatically.

- We can track and record the "most profitable transaction so far" when specifically traversing the timeline from left to right.

    ltr_profit[d] = price[d] - min_price
    left_to_right_max_profit[d] = max(left_to_right_max_profit[d-1], ltr_profit[d])

- we can do the same when traversing the timeline in reverse.

    rtl_profit[d] = max_price - price[d]
    right_to_left_max_profit[d] = max(right_to_left_max_profit[d+1], rtl_profit[d])

- the total profits at any point on the timeline is the sum of these two values

    total_profit[d] = left_to_right_max_profit[d] + right_to_left_max_profit[d]
    
- and the maximum overall profit is the maximum value in that collection.

    maximum_total_profit = max(total_profit)

"""
