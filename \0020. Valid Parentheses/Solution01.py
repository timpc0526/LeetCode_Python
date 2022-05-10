/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 40.87 %
    Runtime : 48 ms
    Memory Usage : 13.8 MB
    Testcase : 91 / 91 passed
    Ranking : 
        Your runtime beats 38.33 % of python3 submissions.
        Your memory usage beats 71.84 % of python3 submissions.
}
*/

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(','}':'{',']':'['}
        l = []
        for i in s:
            if i in dic:
                if not l or l.pop() != dic[i]:
                    return False
            else:
                l.append(i)
        return not l             