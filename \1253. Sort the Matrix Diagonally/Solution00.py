/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 81.35 %
    Runtime : 132 ms
    Memory Usage : 14.3 MB
    Testcase : 15 / 15 passed
    Ranking : 
        Your runtime beats 32.42 % of python3 submissions.
        Your memory usage beats 48.37 % of python3 submissions.
}
*/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        # 119ms ft49.32
        d1, d2 = len(mat), len(mat[0])
        alen = d1*d2
        new = [[0]*d2]*d1
        l = [(x, 0) for x in range(d1-1, 0, -1)] + [(0, x) for x in range(0, d2)]
        out = []
        for x, y in l:
            out.append(mat[x][y])
            while x != d1-1 and y != d2-1:
                x += 1
                y += 1
                out.append(mat[x][y])
            out = sorted(out, reverse=True)
            for j in range(len(out)):
                mat[x][y] = out[j]
                x-=1
                y-=1
            out = []
        return mat
            
        