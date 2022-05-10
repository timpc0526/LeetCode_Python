/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 65.72 %
    Runtime : 132 ms
    Memory Usage : 15.9 MB
    Testcase : 62 / 62 passed
    Ranking : 
        Your runtime beats 65.10 % of python3 submissions.
        Your memory usage beats 35.87 % of python3 submissions.
}
*/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        t = list(s)
        slen = len(s)
        r = []
        l = []
        for i in range(slen):
            if s[i] == '(':
                l.append(i)
            elif l and s[i] == ')':
                l.pop()
            elif not l and s[i] == ')':
                r.append(i)
        a = r + l
        for i in sorted(a, reverse = True):
            t.pop(i)
        return ''.join(t)
        