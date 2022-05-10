/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 67.04 %
    Runtime : 64 ms
    Memory Usage : 14.4 MB
    Testcase : 76 / 76 passed
    Ranking : 
        Your runtime beats 84.14 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 0
        pos = 0
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                neg +=1
        if neg%2 == 0:
            return 1
        else:
            return -1
            
        