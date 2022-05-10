/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 54.07 %
    Runtime : 1108 ms
    Memory Usage : 41.8 MB
    Testcase : 210 / 210 passed
    Ranking : 
        Your runtime beats 82.33 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import numpy as np
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        window_start = 0
        max_profit = 0
        for window_end in range(len(prices)):
            profit = prices[window_end] - prices[window_start]
            while(prices[window_end] < prices[window_start]):
                window_start += 1
            if(profit > max_profit):
                max_profit = profit
        return max_profit
        
        
        
'''     self.prices = prices
        if len(self.prices) == 0:
            return 0
        k = len(prices)
        mini = np.argmin(self.prices)
        maxi = np.argmax(self.prices)
        for i in range(k):
            if maxi > mini:
                return self.prices[maxi]-self.prices[mini]
            elif mini == k:
                mini = self.ifelse_min(mini)
            elif maxi < mini:
                maxi = self.ifelse_max(maxi)
            elif maxi == mini:
                return 0
    def ifelse_max(self,maxi):
        self.prices[maxi] = 0
        maxi_new = np.argmax(self.prices)
        return maxi_new
    def ifelse_min(self,mini):
        self.prices[mini] = 
        mini_new = np.argmin(self.prices)
        return mini_new
    
        for i in range(k-1):
            for j in range(i+1,len(prices)):
                out = np.append(out, np.int0(prices[j]-prices[i]))
        num = max(np.int0(out))
        print(num)
        if num > 0:
            return num
        else:
            return 0'''