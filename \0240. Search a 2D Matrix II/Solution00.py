/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 48.45 %
    Runtime : 263 ms
    Memory Usage : 20.5 MB
    Testcase : 129 / 129 passed
    Ranking : 
        Your runtime beats 32.76 % of python3 submissions.
        Your memory usage beats 13.91 % of python3 submissions.
}
*/

class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        
        # 305ms ft20.68
        d1, d2 = len(mat), len(mat[0])
        for i in range(d1):
            for j in range(d2):
                if mat[i][j] > target:
                    break
                elif mat[i][j] == target:
                    return True
        return False
                