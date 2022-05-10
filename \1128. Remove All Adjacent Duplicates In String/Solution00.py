/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 71.07 %
    Runtime : 79 ms
    Memory Usage : 14.9 MB
    Testcase : 106 / 106 passed
    Ranking : 
        Your runtime beats 84.53 % of python3 submissions.
        Your memory usage beats 15.66 % of python3 submissions.
}
*/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                #print(stack)
                stack.append(c)
        return ''.join(stack)
        
        
        '''out = ""
        slen = len(s)
        for i in range(1, slen):
            if s[i] == s[i-1]:
                return s[:i-2]+s[i+2:]'''