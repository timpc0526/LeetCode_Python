/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 48.05 %
    Runtime : 32 ms
    Memory Usage : 13.8 MB
    Testcase : 113 / 113 passed
    Ranking : 
        Your runtime beats 89.71 % of python3 submissions.
        Your memory usage beats 74.68 % of python3 submissions.
}
*/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # 45ms ft42.77
        news = ""
        newt = ""
        for i in s:
            if i == '#':
                news = news[:-1]
            else:
                news+=i
        for j in t:
            if j == '#':
                newt = newt[:-1]
            else:
                newt += j
        if news == newt:
            return True
        else:
            return False
        