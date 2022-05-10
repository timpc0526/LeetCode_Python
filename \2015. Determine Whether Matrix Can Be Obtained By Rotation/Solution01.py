/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 55.33 %
    Runtime : 87 ms
    Memory Usage : 13.9 MB
    Testcase : 113 / 113 passed
    Ranking : 
        Your runtime beats 10.73 % of python3 submissions.
        Your memory usage beats 77.58 % of python3 submissions.
}
*/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        dim = len(mat)
        #print(dim)
        for _ in range(3):
            new = []
            for i in range(dim):
                row = []
                for j in range(dim, 0, -1):
                    #print(j)
                    #print(mat[j-1][i])
                    row.append(mat[j-1][i])
                new.append(row)
            #print(new)
            if new == target:
                return True
            else:
                mat = new
        return False
            