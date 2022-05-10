/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 59.85 %
    Runtime : 3131 ms
    Memory Usage : 13.9 MB
    Testcase : 57 / 57 passed
    Ranking : 
        Your memory usage beats 29.41 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def beautySum(self, s: str) -> int:
        
        slen = len(s)
        out = 0
        for i in range(slen):
            c = collections.Counter()
            for j in range(i, slen):
                c[s[j]] += 1
                cv = c.values()
                out += max(cv)-min(cv)
        return out
        
        
        # 21002ms ft11.29
        '''slen = len(s)
        out = 0
        for i in range(2, slen+1):
            for j in range(slen-i+1):
                c = collections.Counter(s[j:j+i]).most_common()
                if len(c) == 1:
                    continue
                cal = c[0][1] - c[-1][1]
                out+=cal
        return out'''
        