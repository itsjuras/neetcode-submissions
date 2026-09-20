class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestBuy = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - lowestBuy

            if profit > maxProfit:
                maxProfit = profit

            if lowestBuy > prices[i]:
                lowestBuy = prices[i]
            
        return maxProfit