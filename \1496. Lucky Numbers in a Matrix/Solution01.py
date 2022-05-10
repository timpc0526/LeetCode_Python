/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 70.93 %
    Runtime : 179 ms
    Memory Usage : 14.3 MB
    Testcase : 104 / 104 passed
    Ranking : 
        Your runtime beats 52.09 % of python3 submissions.
        Your memory usage beats 38.06 % of python3 submissions.
}
*/

class Solution:
    def luckyNumbers (self, mat: List[List[int]]) -> List[int]:
        #d1, d2 = len(mat), len(mat[0])
        return list({min(row) for row in mat} & 
                    {max(col) for col in zip(*mat)})
            