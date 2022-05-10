/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 62.59 %
    Runtime : 260 ms
    Memory Usage : 14.8 MB
    Testcase : 113 / 113 passed
    Ranking : 
        Your runtime beats 53.61 % of python3 submissions.
        Your memory usage beats 25.87 % of python3 submissions.
}
*/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for i in range(0,len(isConnected[node])):
                if i != node and isConnected[node][i] == 1 and i not in s:
                    s.add(i)
                    dfs(i)
        
        provinces = 0
        s = set({})
        for i in range(0, len(isConnected)):
            if i not in s:
                s.add(i)
                provinces += 1
                dfs(i)
        return(provinces)
        
        
        '''d1 = len(mat)
        d2 = len(mat[0])
        out = 0
        dic = []
        for i in range(d1):
            for j in range(d2):
                if mat[i][j] == 1:
                    if {i, j} not in dic:
                        dic.append({i, j})
                        
        for i in dic:
            if len(i)
        return len(dic)'''
                    