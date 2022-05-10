/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 34.56 %
    Runtime : 128 ms
    Memory Usage : 14.4 MB
    Testcase : 188 / 188 passed
    Ranking : 
        Your runtime beats 34.60 % of python3 submissions.
        Your memory usage beats 79.62 % of python3 submissions.
}
*/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far, max_end_here, min_end_here = float('-inf'), 1, 1
        for num in nums:
            nxt_max_end = max(num, max_end_here * num, min_end_here * num)
            min_end_here = min(num, max_end_here * num, min_end_here * num)
            max_end_here = nxt_max_end
            max_so_far = max(max_so_far, max_end_here)
        return max_so_far
        
        '''nlen = len(nums)
        print(nums)
        for i in range(nlen):'''
            
        