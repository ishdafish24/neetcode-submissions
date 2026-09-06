class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_diff = 0
        for elem in prices[1:]:
            min_price = min(min_price, elem)
            max_diff = max(max_diff, elem - min_price)
        return max_diff


