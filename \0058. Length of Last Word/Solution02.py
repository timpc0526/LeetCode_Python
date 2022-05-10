/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 37.73 %
    Runtime : 24 ms
    Memory Usage : 14.3 MB
    Testcase : 58 / 58 passed
    Ranking : 
        Your runtime beats 98.14 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = list(s)
        b = s.split()
        print(b)
        k = len(b)
        if b ==[]:
            return 0
        return len(b[k-1])