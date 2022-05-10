/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 55.11 %
    Runtime : 467 ms
    Memory Usage : 15 MB
    Testcase : 42 / 42 passed
    Ranking : 
        Your runtime beats 43.33 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums = list(map(str, nums))
        nums = ''.join(nums)
        nums_list = nums.split('0')
        max_num = 0
        for i in nums_list:
            max_num = max(len(i), max_num)
        return max_num
        
        # 586ms ft10.94
        '''same = 0
        tmp = 0
        nlen = len(nums)
        for i in nums:
            if i>0:
                same+=1
            else:
                tmp = max(tmp, same)
                same = 0
        tmp = max(tmp, same)
        return tmp'''
        
        
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
                    
            
            
        