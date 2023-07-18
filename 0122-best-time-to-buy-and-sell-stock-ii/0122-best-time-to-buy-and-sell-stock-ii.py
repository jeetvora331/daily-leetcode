class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        priceGain = []
        
        for i in range(len(prices) -1):
            if prices[i] < prices[i+1]:
                priceGain.append(prices[i+1] - prices[i])
                
        return sum(priceGain)
        