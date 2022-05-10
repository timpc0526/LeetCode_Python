/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 79.93 %
    Runtime : 32 ms
    Memory Usage : 14.3 MB
    Testcase : 99 / 99 passed
    Ranking : 
        Your runtime beats 86.65 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def replaceDigits(self, s: str) -> str:
        string = "abcdefghijklmnopqrstuvwxyz"
        out = ""
        for i in range(len(s)):
            if i%2 ==1:
                out+=(string[string.find(s[i-1])+int(s[i])])
            else:
                out+=(s[i])
        return out
                