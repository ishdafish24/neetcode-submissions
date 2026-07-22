class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for elem in prices[1:]:
            min_price = min(min_price, elem)
            max_profit = max(max_profit, elem - min_price)
        return max_profit


