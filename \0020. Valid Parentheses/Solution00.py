/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 40.87 %
    Runtime : 50 ms
    Memory Usage : 13.8 MB
    Testcase : 91 / 91 passed
    Ranking : 
        Your runtime beats 33.40 % of python3 submissions.
        Your memory usage beats 98.24 % of python3 submissions.
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