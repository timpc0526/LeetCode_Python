/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 69.39 %
    Runtime : 5700 ms
    Memory Usage : 34 MB
    Testcase : 61 / 61 passed
    Ranking : 
        Your runtime beats 7.14 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import numpy as np
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        out_list = []
        for i in nums:
            if i not in out_list:
                out_list = np.append(out_list,i)
            else:
                for j in range(len(out_list)):
                    if i == out_list[j]:
                        out_list = np.delete(out_list,j)
                        break
        return np.int0(out_list[0])