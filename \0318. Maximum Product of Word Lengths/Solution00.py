/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 56.67 %
    Runtime : 880 ms
    Memory Usage : 15.8 MB
    Testcase : 167 / 167 passed
    Ranking : 
        Your memory usage beats 19.24 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

#import itertools
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        S = list(map(set, words))
        for i in range(len(words)):
            for j in range(i):
                if not S[i] & S[j]: # O(26 * 26) = O(1)
                    ans = max(ans, len(words[i] * len(words[j])))
        return ans
        
        
        # 1390ms ft47.31
        '''result = itertools.combinations(words, 2)
        maxnum = 0
        for i in result:
            s = True
            for j in i[0]:
                if j in i[1]:
                    s = False
                    break
            if s:
                maxnum = max(maxnum, len(i[0])*len(i[1]))
        return maxnum'''
            
            
        
        