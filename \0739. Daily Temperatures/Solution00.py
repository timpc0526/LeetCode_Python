/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 67.17 %
    Runtime : 1196 ms
    Memory Usage : 24.5 MB
    Testcase : 47 / 47 passed
    Ranking : 
        Your runtime beats 95.96 % of python3 submissions.
        Your memory usage beats 90.97 % of python3 submissions.
}
*/

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # 1756ms ft40.62
        stack = []
        tlen = len(temp)
        out = [0] * tlen
        for i in range(tlen):
            while stack and temp[stack[-1]] < temp[i]:
                num = stack.pop()
                out[num] = i - num
            stack.append(i)
        return out