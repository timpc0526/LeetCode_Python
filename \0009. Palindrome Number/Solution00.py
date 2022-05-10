/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 52.40 %
    Runtime : 72 ms
    Memory Usage : 14.3 MB
    Testcase : 11510 / 11510 passed
    Ranking : 
        Your runtime beats 70.74 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x = str(x)
            y = x[::-1]
            if x == y:
                return True