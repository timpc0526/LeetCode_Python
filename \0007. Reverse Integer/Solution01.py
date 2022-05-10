/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 26.71 %
    Runtime : 24 ms
    Memory Usage : 14 MB
    Testcase : 1032 / 1032 passed
    Ranking : 
        Your runtime beats 99.22 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def reverse(self, x: int) -> int:
            num = str(abs(x))
            num = int(num[::-1])
            if num > 2147483647:
                return 0
            if x<0:
                num = -num
            return num

        
        

            