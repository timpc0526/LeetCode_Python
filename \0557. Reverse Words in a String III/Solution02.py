/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 78.78 %
    Runtime : 64 ms
    Memory Usage : 15 MB
    Testcase : 29 / 29 passed
    Ranking : 
        Your runtime beats 44.64 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split(' ')
        new =[]
        for i in slist:
            new.append(i[::-1])
        return ' '.join(new)
        