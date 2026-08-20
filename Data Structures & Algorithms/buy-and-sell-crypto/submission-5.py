class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]-mini>profit:
                profit = prices[i]-mini
            if prices[i]<mini:
                mini = prices[i]
        return profit

        #take first price as minimum 
        #loop from index 1 
        # if price[i] - mimium > profit wwe have , update profit
        # update minimum every index




        