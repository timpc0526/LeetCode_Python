/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 66.62 %
    Runtime : 539 ms
    Memory Usage : 14.6 MB
    Testcase : 63 / 63 passed
    Ranking : 
        Your memory usage beats 27.00 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        result = [-1] * n
        for i in range(n):
            c = i
            for r in range(m):
                nxt = c + grid[r][c]
                if nxt in (-1, n) or grid[r][c] != grid[r][nxt]: break
                c = nxt
                print(c)
            else:
                result[i] = c
        return result
        
        '''d1, d2 = len(grid), len(grid[0])
        #print(grid)
        out = []
        final =[]
        dic = {}
        for i in range(d1):
            for j in range(1, d2):
                
                if grid[i][j] == grid[i][j-1] == 1:
                    if i == 0:
                        dic[j-1] = 1
                    else:
                        if 
                    out.append((j-1, 1))
                elif grid[i][j] == grid[i][j-1] == -1:
                    if i = 0:
                        dic[j-1] = -1
                    else:
                        j-1 in dic:
                            
                    out.append((j, -1))
            final.append(out)
            out = []'''
                
            