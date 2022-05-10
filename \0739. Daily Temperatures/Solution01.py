/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 67.17 %
    Runtime : 1756 ms
    Memory Usage : 24.7 MB
    Testcase : 47 / 47 passed
    Ranking : 
        Your runtime beats 29.79 % of python3 submissions.
        Your memory usage beats 84.11 % of python3 submissions.
}
*/

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # 1844ms ft33.7
        stack = []
        tlen = len(temp)
        out = [0] * tlen
        for i in range(tlen):
            while stack and temp[stack[-1]] < temp[i]:
                num = stack.pop()
                out[num] = i - num
            stack.append(i)
        return out