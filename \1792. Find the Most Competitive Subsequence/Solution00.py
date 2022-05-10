/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 48.46 %
    Runtime : 1764 ms
    Memory Usage : 27.5 MB
    Testcase : 88 / 88 passed
    Ranking : 
        Your runtime beats 51.55 % of python3 submissions.
        Your memory usage beats 41.93 % of python3 submissions.
}
*/

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # 1546ms ft74
        nlen = len(nums)
        stack = []
        for index, i in enumerate(nums):
            while stack and i < stack[-1] and nlen-index+len(stack)>k:
                stack.pop()
            if len(stack) < k:
                stack.append(i)
            #print(stack)
        '''if len(stack) == k: return stack
        if stack[-1] < stack[-2]:
            stack.pop(-2)
        else:
            stack.pop()'''
        return stack
            
            