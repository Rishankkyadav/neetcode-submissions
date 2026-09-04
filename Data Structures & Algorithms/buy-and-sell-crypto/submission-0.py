class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # remeber the cheapest bp and find the highest sp
        l , r = 0 , 1
        max_profit = 0
        for r in range(len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(profit , max_profit)
            else:
                l = r
                r += 1
        return max_profit


            




        