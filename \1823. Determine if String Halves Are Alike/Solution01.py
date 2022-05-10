/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 78.00 %
    Runtime : 50 ms
    Memory Usage : 14.2 MB
    Testcase : 113 / 113 passed
    Ranking : 
        Your runtime beats 49.64 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        slen = len(s)//2
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        a = s[:slen]
        b = s[slen:]
        a_num = 0
        b_num = 0
        for i, j in zip(a, b):
            if i in vowels:
                a_num += 1
            if j in vowels:
                b_num += 1
        if a_num == b_num:
            return True
        else:
            return False
        return True