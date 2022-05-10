/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 45.86 %
    Runtime : 47 ms
    Memory Usage : 14.4 MB
    Testcase : 130 / 130 passed
    Ranking : 
        Your runtime beats 41.77 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []
        for i, j in zip(s1, s2):
            if i != j:
                diff.append((i, j))
        print(diff)
        if len(diff) == 0:
            return True
        if len(diff)==2 and diff[0][::-1] == diff[1]:
            return True
        else:
            return False
        