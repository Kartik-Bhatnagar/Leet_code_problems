#URL : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#[Easy] [121] 
#Title: [Best Time to Buy and Sell Stock]
#Author: Kartik Bhatnagar
#Date : 2024-08-17 (YYYY-MM-DD)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices)<2:
            return 0
        cur_min = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            max_profit = max(max_profit,prices[i]-cur_min)
            cur_min = min(prices[i],cur_min)
        return max_profit

if __name__ == "__main__":
    s=Solution()
    prices = [7,1,5,3,6,4]
    print(s.maxProfit(prices))