/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 32.40 %
    Runtime : 32 ms
    Memory Usage : 13.9 MB
    Testcase : 136 / 136 passed
    Ranking : 
        Your runtime beats 85.03 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(' ')
        s2 = sentence2.split(' ')
        while s1 and s2 and s1[0] == s2[0]:
            s1 = s1[1:]
            s2 = s2[1:]
        while s1 and s2 and s1[-1] == s2[-1]:
            s1.pop()
            s2.pop()
        return not s1 or not s2
            
        