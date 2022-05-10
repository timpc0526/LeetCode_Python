/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 61.47 %
    Runtime : 76 ms
    Memory Usage : 15.2 MB
    Testcase : 36 / 36 passed
    Ranking : 
        Your runtime beats 37.14 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        