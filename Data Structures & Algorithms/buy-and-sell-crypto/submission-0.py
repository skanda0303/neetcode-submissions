class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = prices[0]
        maxprofit = 0
        for i in range(1,len(prices)):
            profit = prices[i] - price
            maxprofit = max(profit,maxprofit)
            if prices[i] < price:
                price = prices[i]

        return maxprofit
        
            