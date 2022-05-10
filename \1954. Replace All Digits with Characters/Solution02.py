/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 79.93 %
    Runtime : 42 ms
    Memory Usage : 14.3 MB
    Testcase : 99 / 99 passed
    Ranking : 
        Your runtime beats 50.11 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def replaceDigits(self, s: str) -> str:
        string = "abcdefghijklmnopqrstuvwxyz"
        slen = len(s)
        out = ""
        for i in range(slen):
            if i%2 ==1:
                out+=(string[string.find(s[i-1])+int(s[i])])
            else:
                out+=(s[i])
        return out
                