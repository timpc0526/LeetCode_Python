/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 59.09 %
    Runtime : 706 ms
    Memory Usage : 22.3 MB
    Testcase : 33 / 33 passed
    Ranking : 
        Your runtime beats 6.92 % of python3 submissions.
        Your memory usage beats 69.33 % of python3 submissions.
}
*/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #nlen = len(nums)
        #nums = list(set(nums))
        
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])
        return [i + 1 for i, num in enumerate(nums) if num > 0]
        
        
        
        # Time limit exceeded
        '''nlen = len(nums)
        no = []
        for i in range(1, nlen+1):
            if i not in nums:
                no.append(i)
        return no'''
        