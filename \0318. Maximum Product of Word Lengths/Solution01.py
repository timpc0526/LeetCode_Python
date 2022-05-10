/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 56.67 %
    Runtime : 1409 ms
    Memory Usage : 14.2 MB
    Testcase : 167 / 167 passed
    Ranking : 
        Your memory usage beats 94.75 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import itertools
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        # 1390ms ft47.31
        result = itertools.combinations(words, 2)
        maxnum = 0
        for i in result:
            s = True
            for j in i[0]:
                if j in i[1]:
                    s = False
                    break
            if s:
                maxnum = max(maxnum, len(i[0])*len(i[1]))
        return maxnum
            
            
        
        