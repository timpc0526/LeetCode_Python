/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 62.46 %
    Runtime : 197 ms
    Memory Usage : 14.7 MB
    Testcase : 57 / 57 passed
    Ranking : 
        Your runtime beats 7.92 % of python3 submissions.
        Your memory usage beats 81.80 % of python3 submissions.
}
*/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        out = []
        out2 = []
        flat = []
        num = 0
        #dim1, dim2 = len(mat), len(mat[0])
        #print((dim1, dim2))
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
                
        return out
        