class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, max_prof = prices[0], 0
        for price in prices:
            lowest = min(lowest, price)
            max_prof = max(price - lowest, max_prof)
        return max_prof