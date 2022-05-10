/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 81.29 %
    Runtime : 21 ms
    Memory Usage : 14.2 MB
    Testcase : 72 / 72 passed
    Ranking : 
        Your runtime beats 99.11 % of python3 submissions.
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
        
        
        