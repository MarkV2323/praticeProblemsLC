"""
Author: Mark Vincent II
For LeetCode problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Problem Statement:
Given an array, prices. i = ith day, prices[i] = price value. Want to maximize your profit by
choosing a single day to buy, and another day to sell. Cannot go back in time.

Problem Solution:
1: Loop through the price list.
2: Get the maximum value after the ith iteration of the price list.
3: Calculate the current max profit from the maximum price - price.
4: If this value is > max_profit, set it as the new value, otherwise disregard and move to next iteration.

O(n) version:
Go back in time! (max_profit2)
"""


class Solution:
    @staticmethod
    def max_profit2(prices: list[int]) -> int:
        max_profit = 0
        high_sale_price = prices[len(prices)-1]
        for i, price in enumerate(prices[::-1]):
            if price > high_sale_price:
                high_sale_price = price
            if max_profit < (high_sale_price - price):
                max_profit = (high_sale_price - price)
        return max_profit

    @staticmethod
    def max_profit(prices: list[int]) -> int:
        max_profit = 0
        for i, price in enumerate(prices):
            current_profit = max(prices[i:]) - price
            if current_profit > max_profit:
                max_profit = current_profit
        return max_profit


sol = Solution()
priceIn = [7, 6, 4, 3, 1]
print(f"Max Profit: {sol.max_profit2(priceIn)}")
