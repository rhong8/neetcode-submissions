class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #two pointers:
        l = 0
        r = 1
        maxProfit = 0
        #l moves only if r finds a value smaller than it
        while r < len(prices):
            maxProfit = max(maxProfit, prices[r] - prices[l])
            print(maxProfit)
            
            print(f"r:{r}")
            if prices[r] < prices[l]:
                l = r
            r += 1

        return maxProfit
