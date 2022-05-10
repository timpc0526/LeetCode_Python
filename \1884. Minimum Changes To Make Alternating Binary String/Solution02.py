/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 59.18 %
    Runtime : 80 ms
    Memory Usage : 14.3 MB
    Testcase : 89 / 89 passed
    Ranking : 
        Your runtime beats 38.50 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def minOperations(self, s: str) -> int:
        
        slen = len(s)
        out1 = 0
        out2 = 0
        s0, s1 = '0', '1'
        for i in range(slen):
            if i%2 == 0:
                if s[i] != s0:
                    out1 += 1
                else:
                    out2 += 1
            else:
                if s[i] != s1:
                    out1 += 1
                else:
                    out2 += 1
        return min(out1, out2)
        