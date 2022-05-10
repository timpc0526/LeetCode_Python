/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 68.02 %
    Runtime : 141 ms
    Memory Usage : 13.8 MB
    Testcase : 483 / 483 passed
    Ranking : 
        Your runtime beats 27.07 % of python3 submissions.
        Your memory usage beats 79.48 % of python3 submissions.
}
*/

class Solution:
    def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
        d1, d2, = len(mat), len(mat[0])
        for i in range(1, d1):
            if mat[i-1][:d2-1] != mat[i][1:]:
                return False
        return True
            
        
        '''d1, d2, = len(mat), len(mat[0])
        jump = d2+1
        print((d1, d2))
        flat = []
        for i in range(d1):
            for j in range(d2):
                flat.append(mat[i][j])
        flen = (d1*d2)
        for i in range(flen//2):
            if i == d2-1 or i == flen-d2:
                print(flat[i])
                continue
            c = flen//(i+jump)
            #print(c)
            for k in range(c):
                if flat[i+k*jump] != flat[i+(k+1)*jump]:
                    return False
        return True'''
        