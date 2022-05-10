/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 65.37 %
    Runtime : 32 ms
    Memory Usage : 13.9 MB
    Testcase : 86 / 86 passed
    Ranking : 
        Your runtime beats 87.05 % of python3 submissions.
        Your memory usage beats 62.77 % of python3 submissions.
}
*/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack, score = [], 0
        for c in s:
            if c == '(':
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(2 * score, 1)
        return score
        
        # 38ms ft66.83
        '''sym = ['(',')']
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
        return sum(s)'''