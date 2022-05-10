/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 65.72 %
    Runtime : 121 ms
    Memory Usage : 15.8 MB
    Testcase : 62 / 62 passed
    Ranking : 
        Your runtime beats 73.31 % of python3 submissions.
        Your memory usage beats 61.58 % of python3 submissions.
}
*/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        t, stack = list(s), []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    t[i] = ''
        for i in stack:
            t[i] = ''
        return ''.join(t)
        
        
        # 113ms ft82.55
        '''t = list(s)
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
        return ''.join(t)'''
        