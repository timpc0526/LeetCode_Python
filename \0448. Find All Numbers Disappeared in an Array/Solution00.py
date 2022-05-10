/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 59.09 %
    Runtime : 392 ms
    Memory Usage : 41.8 MB
    Testcase : 33 / 33 passed
    Ranking : 
        Your runtime beats 72.90 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import numpy as np
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 408ms ft21.94
        allnums = set(range(1, len(nums)+1))
        nums = set(nums)
        no = allnums - nums
        return list(no)
        
        
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
        