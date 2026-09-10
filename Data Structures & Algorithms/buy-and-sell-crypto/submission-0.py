class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, cheap = 0, prices[0]
        for price in prices:
            profit = max(profit, price - cheap)
            cheap = min(cheap, price)
        return profit