/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 62.46 %
    Runtime : 138 ms
    Memory Usage : 14.6 MB
    Testcase : 57 / 57 passed
    Ranking : 
        Your runtime beats 36.04 % of python3 submissions.
        Your memory usage beats 98.92 % of python3 submissions.
}
*/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if r * c != m * n: return mat
        ans = [[0] * c for _ in range(r)]
        i, j = 0, 0
        for row in mat:
            for cell in row:
                ans[i][j] = cell
                j += 1
                if j == c:
                    i, j = i + 1, 0
        return ans
        
        
        
        # 99ms ft60.31
        '''out = []
        out2 = []
        flat = []
        num = 0
        for i in mat:
            for j in i:
                flat.append(j)
        if r*c != len(flat):
            return mat
        else:
            for m in range(r):
                for n in range(c):
                    out2.append(flat[num])
                    num += 1
                out.append(out2)
                out2 = []
        return out'''
        