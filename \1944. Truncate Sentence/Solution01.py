/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 81.29 %
    Runtime : 38 ms
    Memory Usage : 14.3 MB
    Testcase : 72 / 72 passed
    Ranking : 
        Your runtime beats 61.93 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        slist = s.split(' ')
        if len(slist) == k:
            return s
        else:
            return ' '.join(slist[:k])
        
        
        