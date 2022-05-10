/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 61.47 %
    Runtime : 72 ms
    Memory Usage : 15.1 MB
    Testcase : 36 / 36 passed
    Ranking : 
        Your runtime beats 43.17 % of python3 submissions.
        Your memory usage beats 12.04 % of python3 submissions.
}
*/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #76ms ft37.8
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        