/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 55.11 %
    Runtime : 162 ms
    Memory Usage : 13.8 MB
    Testcase : 507 / 507 passed
    Ranking : 
        Your runtime beats 24.46 % of python3 submissions.
        Your memory usage beats 99.10 % of python3 submissions.
}
*/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        trans = []
        m, n = len(board), len(board[0])
        for i in zip(*board):
            trans.append(i)
        for i in range(m):
            a = collections.Counter(board[i])
            b = collections.Counter(trans[i])
            #print(a.values())
            #print(b.values())
            if sum(i>1 for i in a.values()) > 1 or sum(i>1 for i in b.values()) > 1:
                return False
        check = []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    check += trans[k+3*i][0+3*j:3+3*j]
                    c = collections.Counter(check)
                    if sum(i>1 for i in c.values()) > 1:
                        return False
                check = []
        return True
                    
        