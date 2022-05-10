/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 40.80 %
    Runtime : 46 ms
    Memory Usage : 14 MB
    Testcase : 191 / 191 passed
    Ranking : 
        Your runtime beats 38.05 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s
        