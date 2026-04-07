class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        mp = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            mp = max(mp, prices[r] - prices[l])
        return mp
        
            