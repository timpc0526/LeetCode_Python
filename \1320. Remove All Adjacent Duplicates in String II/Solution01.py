/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 56.26 %
    Runtime : 210 ms
    Memory Usage : 18.9 MB
    Testcase : 20 / 20 passed
    Ranking : 
        Your runtime beats 28.62 % of python3 submissions.
        Your memory usage beats 17.76 % of python3 submissions.
}
*/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                if stack[-1][1] == k - 1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([c, 1])
        return ''.join(c * v for c, v in stack)
    
    
        # Time Limit Exceeded
        '''stack = []
        for i in s:
            stack.append(i)
            while len(set(stack[-k:])) == 1 and len(stack) >= k:
                stack = stack[:-k]
        return ''.join(stack)'''
        