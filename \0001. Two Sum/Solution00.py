/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 48.57 %
    Runtime : 108 ms
    Memory Usage : 31.1 MB
    Testcase : 53 / 53 passed
    Ranking : 
        Your runtime beats 47.93 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import numpy as np
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num2 = target - nums[i]
            num1 = nums[i]
            nums[i] = None
            if num2 in nums[i+1:]:
                break
        return i, nums.index(num2)