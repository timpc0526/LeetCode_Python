/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 59.09 %
    Runtime : 777 ms
    Memory Usage : 41.7 MB
    Testcase : 33 / 33 passed
    Ranking : 
        Your runtime beats 00.00 % of submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import numpy as np
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 408ms ft21.94
        allnums = set(range(1, len(nums)+1))
        nums = set(nums)
        return list(allnums - nums)
        
        
        # 706ms ft5.02
        '''for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])
        return [i + 1 for i, num in enumerate(nums) if num > 0]'''
        
        # Time limit exceeded
        '''nlen = len(nums)
        no = []
        for i in range(1, nlen+1):
            if i not in nums:
                no.append(i)
        return no'''
        