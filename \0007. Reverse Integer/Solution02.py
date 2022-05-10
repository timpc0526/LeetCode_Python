/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 26.71 %
    Runtime : 36 ms
    Memory Usage : 14.2 MB
    Testcase : 1032 / 1032 passed
    Ranking : 
        Your runtime beats 80.30 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(abs(x))
            x = list(x)[::-1]
            qq = ''
            x = int(qq.join(x))
            if x > 2**31-1 or x < -2**31:
                return 0
            return -x
        elif x >= 0:
            x = str(x)
            x = list(x)[::-1]
            qq = ''
            x = int(qq.join(x))
            if x > 2**31-1 or x < -2**31:
                return 0
            return x
            