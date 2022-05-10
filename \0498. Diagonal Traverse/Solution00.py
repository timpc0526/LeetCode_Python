/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 56.84 %
    Runtime : 274 ms
    Memory Usage : 17.6 MB
    Testcase : 32 / 32 passed
    Ranking : 
        Your runtime beats 41.03 % of python3 submissions.
        Your memory usage beats 58.28 % of python3 submissions.
}
*/

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # 269ms ft49.39
        if not any(matrix): return []
        m, n = len(matrix), len(matrix[0])
        r, c, result = 0, 0, []
        for _ in range(m * n):
            result.append(matrix[r][c])
            if (r + c) % 2 == 0:
                r -= 1
                c += 1
                if c >= n:
                    r += 2
                    c -= 1
                elif r < 0:
                    r += 1
            else:
                r += 1
                c -= 1
                if r >= m:
                    c += 2
                    r -= 1
                elif c < 0:
                    c += 1
        return result
        
        '''d1, d2 = len(mat), len(mat[0])
        if d1 ==1:
            return mat[0]
        elif d2 ==1:
            return [x[0] for x in mat]
        out = []
        right = True
        r, c = 0, 0
        while len(out) != d1*d2:
            out.append(mat[r][c])
            if right == True and r != 0 and c != d1-1:
                r -= 1
                c += 1
            elif right == False and r != d1-1 and c != 0:
                r += 1
                c -= 1
            elif right == True and r == 0 and c < d1-1:
                c += 1
                right = False
                
            elif right == True and c == d1-1:
                r += 1
                right = False
            
            elif right == False and c == 0 and r < d1-1:
                r += 1
                right = True
                
            elif right == False and r == d1-1:
                c += 1
                right = True
            
        return out'''
        
        
        '''d1, d2 = len(mat), len(mat[0])
        out = []
        r, c = 0, 0
        right = True
        bound = [-1, d1]
        while len(out) != d1*d2:
            if r in bound or c in bound:
                if r == -1 and c == d1 and right:
                    r += 2
                    c -= 1
                    right = False
                    continue
                if right:
                    right = False
                else:
                    right = True
                
                if r == -1:
                    r += 1
                if r == d1:
                    r -= 1
                if c == -1:
                    c += 1
                if c == d1:
                    c -= 1
                continue
            else:
                print((r, c))
                out.append(mat[r][c])
                
                
            if right and r not in [0, d1-1] and c not in [0, d1-1]:
                r -= 1
                c += 1
            elif left and r not in [0, d1-1] and c not in [0, d1-1]:
                r += 1
                c -= 1
            elif right and r == 0 and c == 0:
                c += 1
            elif right
            
            
        print(out)'''
            
            