class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # priceGain = []
        gain = 0
        
        for i in range(len(prices) -1):
            if prices[i] < prices[i+1]:
                gain += prices[i+1] - prices[i]
                # priceGain.append(prices[i+1] - prices[i])
                
        return gain
        