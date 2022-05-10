/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 47.25 %
    Runtime : 152 ms
    Memory Usage : 14 MB
    Testcase : 152 / 152 passed
    Ranking : 
        Your memory usage beats 31.77 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        B = 0
        temp_a = []
        temp_b = []
        for i, j in zip(secret, guess):
            if i == j:
                A += 1
            else:
                temp_a.append(i)
                temp_b.append(j)
        for i in temp_a:
            if i in temp_b:
                B+=1
                temp_b.remove(i)
        A, B = map(str, (A, B))
        return A+'A'+B+'B'
                