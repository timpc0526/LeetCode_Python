/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 67.04 %
    Runtime : 123 ms
    Memory Usage : 14.3 MB
    Testcase : 76 / 76 passed
    Ranking : 
        Your runtime beats 8.76 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        # 64ms ft52.76
        neg = 0
        #pos = 0
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                neg +=1
        if neg%2 == 0:
            return 1
        else:
            return -1
            
        