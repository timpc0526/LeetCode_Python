/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 75.58 %
    Runtime : 28 ms
    Memory Usage : 14 MB
    Testcase : 73 / 73 passed
    Ranking : 
        Your runtime beats 98.12 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import collections
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # 58ms ft26.03
        out = 0
        count = collections.Counter(nums)
        for i in count:
            if count[i] == 1:
                out += i
        return out
        