/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 67.17 %
    Runtime : 1844 ms
    Memory Usage : 24.8 MB
    Testcase : 47 / 47 passed
    Ranking : 
        Your runtime beats 23.54 % of python3 submissions.
        Your memory usage beats 69.90 % of python3 submissions.
}
*/

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        tlen = len(temp)
        out = [0] * tlen
        for i in range(tlen):
            while stack and temp[stack[-1]] < temp[i]:
                num = stack.pop()
                out[num] = i - num
            stack.append(i)
        return out