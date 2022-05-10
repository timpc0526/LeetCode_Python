/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 75.58 %
    Runtime : 58 ms
    Memory Usage : 13.8 MB
    Testcase : 73 / 73 passed
    Ranking : 
        Your runtime beats 25.75 % of python3 submissions.
        Your memory usage beats 56.62 % of python3 submissions.
}
*/

import collections
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        out = 0
        count = collections.Counter(nums)
        for i in count:
            if count[i] == 1:
                out += i
        return out
        