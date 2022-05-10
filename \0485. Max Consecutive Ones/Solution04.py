/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 55.11 %
    Runtime : 586 ms
    Memory Usage : 14.4 MB
    Testcase : 42 / 42 passed
    Ranking : 
        Your runtime beats 16.74 % of python3 submissions.
        Your memory usage beats 8.73 % of python3 submissions.
}
*/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        same = 0
        tmp = 0
        nlen = len(nums)
        for i in nums:
            if i>0:
                same+=1
            else:
                tmp = max(tmp, same)
                same = 0
        tmp = max(tmp, same)
        return tmp
        
        
        '''same = 0
        tmp = 0
        nlen = len(nums)
        if nlen == 1:
            return 0
        for i in range(nlen-1):
            if nums[i] == nums[i+1]:
                same+=1
            else:
                tmp = max(tmp, same)
                same = 0
        tmp = max(tmp, same)
        return tmp'''
                    
            
            
        