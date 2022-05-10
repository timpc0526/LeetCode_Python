/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 65.70 %
    Runtime : 424 ms
    Memory Usage : 21.1 MB
    Testcase : 63 / 63 passed
    Ranking : 
        Your runtime beats 90.81 % of python3 submissions.
        Your memory usage beats 37.58 % of python3 submissions.
}
*/

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        flen = len(flips)
        out = 0
        maxnum = 0
        for i, flip in enumerate(flips):
            maxnum = max(flip, maxnum)
            if maxnum == i+1:
                out += 1
        return out
                
                
        
        #time limit exceeded
        '''flen = len(flips)
        s = [0] * flen
        out = 0
        for i, flip in enumerate(flips):
            s[flip-1] = 1
            if 0 not in s[:i+1] and 1 not in s[i+1:]:
                out += 1
        return out'''