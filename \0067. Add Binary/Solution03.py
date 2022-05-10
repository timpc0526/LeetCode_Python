/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 50.49 %
    Runtime : 40 ms
    Memory Usage : 14.3 MB
    Testcase : 294 / 294 passed
    Ranking : 
        Your runtime beats 69.99 % of python3 submissions.
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
        print(type(d))
        print(e)
        #print(a+b)
        return e
    #def dtob(self):
        