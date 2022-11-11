import sys

def find_best_trade(prices):
    maxProfit, buyPoint = 0, 0
    for index in range(0, len(prices)):
        if prices[index] - prices[buyPoint] <= 0:
            buyPoint = index
        else:
            maxProfit = max(maxProfit, prices[index] - prices[buyPoint])
    return maxProfit

def find_min_max(prices):
    curMax, curMin = -sys.maxsize, sys.maxsize
    for price in prices:
        curMax = max(curMax, price)
        curMin = min(curMin, price)
    return max(curMax - curMin, 0)
