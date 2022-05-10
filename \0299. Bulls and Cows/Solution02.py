/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 47.25 %
    Runtime : 121 ms
    Memory Usage : 14.1 MB
    Testcase : 152 / 152 passed
    Ranking : 
        Your runtime beats 00.00 % of submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 152ms ft5.06
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
                