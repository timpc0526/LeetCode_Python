/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 65.37 %
    Runtime : 38 ms
    Memory Usage : 13.9 MB
    Testcase : 86 / 86 passed
    Ranking : 
        Your runtime beats 67.34 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        i = 0
        sym = ['(',')']
        s = list(s.replace('()', '1'))
        if len(s) == 1: return int(s[0])
        while len(s) >1:
            for i in range(len(s)):
                if s[i] not in sym and s[i+1] not in sym:
                    s[i] = int(s[i]) + int(s[i+1])
                    s.pop(i+1)
                    break
                if s[i] == '(' and s[i+2] == ')':
                    s[i+1] = int(s[i+1])*2
                    s.pop(i+2)
                    s.pop(i)
                    break
        return sum(s)