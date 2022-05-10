/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 62.05 %
    Runtime : 340 ms
    Memory Usage : 31.9 MB
    Testcase : 200 / 200 passed
    Ranking : 
        Your runtime beats 00.00 % of submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import numpy as np
class Solution:
    #def maxProfit(self, prices: List[int]) -> int:
        
    
    
    def maxProfit(self, prices: List[int]) -> int:  ##94.4%
        mini = 0
        output = 0
        out_list = []
        for i in range(len(prices)):
            profit = prices[i] - prices[mini]
            mini = i
            out_list = np.append(out_list,profit)
        for x in out_list:
            if x > 0:
                output+=x
        return np.int0(output)