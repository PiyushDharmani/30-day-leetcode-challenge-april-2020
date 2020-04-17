class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # i=0
        # prices.append(0)
        # while i < (len(prices)-1):
        #     print(i)
        #     if prices[i+1] > prices[i]:
        #         buy = i
        #         while (prices[i+1] > prices[i]):
        #             i+=1
        #             print(i)
        #         max_profit+=(prices[i]-prices[buy])
        #     i+=1
        # return max_profit


        # max_profit=0
        # for i in range(1,len(prices)):
        #     if prices[i] > prices[i-1]:
        #         max_profit+=prices[i]-prices[i-1]
        # return max_profit

        max_profit=0
        for i in range(1,len(prices)):
            max_profit+=max(0,prices[i]-prices[i-1])
        return max_profit

    
