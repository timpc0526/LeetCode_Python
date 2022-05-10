/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 42.11 %
    Runtime : 59 ms
    Memory Usage : 14.2 MB
    Testcase : 43 / 43 passed
    Ranking : 
        Your runtime beats 45.54 % of python3 submissions.
        Your memory usage beats 89.16 % of python3 submissions.
}
*/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 40ms ft87.84
        s2t = {}
        t2s = {}
        for i, j in zip(s, t):
            if i in s2t.keys():
                if s2t[i] != j:
                    return False
            elif j in t2s.keys():
                if t2s[j] != i:
                    return False
            else:
                s2t[i] = j
                t2s[j] = i
        return True
                