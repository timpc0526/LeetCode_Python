/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 57.65 %
    Runtime : 868 ms
    Memory Usage : 27.1 MB
    Testcase : 51 / 51 passed
    Ranking : 
        Your runtime beats 54.88 % of python3 submissions.
        Your memory usage beats 34.88 % of python3 submissions.
}
*/

import itertools
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #nlen = len(nums)
        #c = collections.Counter(nums)
        #r2 = itertools.combinations(nums, 2)
        
        # 1250ms ft10.52
        c = collections.Counter()
        out = 0
        for i in nums:
            #print(c)
            if i in c:
                out+=1
                if c[i] ==1:
                    del c[i]
                else:
                    c[i] -= 1
            else:
                c[k-i] += 1
            
            
        return out
        
        
        
        
                
                
        #print(sum([i+j == k for i, j in result]))
        #return sum([i+j == k for i, j in result])