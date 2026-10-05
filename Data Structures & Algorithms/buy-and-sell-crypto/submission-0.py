class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=0
        maxp= 0

        for s in range(len(prices)):
            if prices[s] < prices[b]:
                b = s
            maxp = max(maxp, prices[s] - prices[b])
        return maxp
