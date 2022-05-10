/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 48.45 %
    Runtime : 305 ms
    Memory Usage : 20.4 MB
    Testcase : 129 / 129 passed
    Ranking : 
        Your runtime beats 17.60 % of python3 submissions.
        Your memory usage beats 42.13 % of python3 submissions.
}
*/

class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        d1, d2 = len(mat), len(mat[0])
        for i in range(d1):
            for j in range(d2):
                if mat[i][j] > target:
                    break
                elif mat[i][j] == target:
                    return True
        return False
                