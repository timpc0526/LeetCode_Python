/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 50.49 %
    Runtime : 32 ms
    Memory Usage : 14.1 MB
    Testcase : 294 / 294 passed
    Ranking : 
        Your runtime beats 92.38 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        c = a+b
        d = bin(c)
        e = d[2:]
        #print(a+b)
        return e
    #def dtob(self):
        