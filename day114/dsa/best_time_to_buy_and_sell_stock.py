"""
DSA Problem: Best Time to Buy and Sell Stock
Given an array for which the ith element is the price of a given stock on day i, find the maximum profit.
"""

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print("Max profit:", max_profit(prices))  # Output: 5
