/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 52.70 %
    Runtime : 5704 ms
    Memory Usage : 16.2 MB
    Testcase : 206 / 206 passed
    Ranking : 
        Your memory usage beats 12.36 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        #snums = sorted(nums)
        snums = sorted(list(set(nums)))
        slen = len(snums)
        maxnum = 0
        for i in range(1, slen):
            if snums[i-1] - snums[i] == -1:
                maxnum = max(maxnum, nums.count(snums[i-1])+nums.count(snums[i]))
        return maxnum
            
        
        
        
        
        # 9108ms ft5.12
        '''snums = sorted(list(set(nums)))
        dic = dict((i, nums.count(i)) for i in snums)
        maxnum = 0
        for i in range(1, len(snums)):
            if snums[i-1]-snums[i] == -1:
                maxnum = max(maxnum, dic[snums[i-1]]+dic[snums[i]])
        return maxnum'''