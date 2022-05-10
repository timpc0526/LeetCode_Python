/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 77.70 %
    Runtime : 72 ms
    Memory Usage : 14 MB
    Testcase : 103 / 103 passed
    Ranking : 
        Your runtime beats 52.08 % of python3 submissions.
        Your memory usage beats 8.84 % of python3 submissions.
}
*/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        A, B = map(set, zip(*paths))
        return (B - A).pop()
        
        
        '''out = None
        for i in paths:
            if out == None:
                out = i[1]
            if i[0] == out:
                out = i[1]
        return out'''
        