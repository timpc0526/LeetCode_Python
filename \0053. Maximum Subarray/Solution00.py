/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 49.52 %
    Runtime : 124 ms
    Memory Usage : 31.9 MB
    Testcase : 203 / 203 passed
    Ranking : 
        Your runtime beats 00.00 % of submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import numpy as np
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = 0
        num = 0
        num_list = []
        neg = nums[0]
        k = len(nums)
        if k == 1:
            return nums[0]
        for i in range(k):
            num += nums[i]
            if num > maxi:
                maxi = num
            elif num <= 0:
                if num > neg:
                    neg = num
                
                num = 0
        if maxi > 0:
            return maxi
        else:
            return neg
            