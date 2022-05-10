/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 38.60 %
    Runtime : 216 ms
    Memory Usage : 25.4 MB
    Testcase : 38 / 38 passed
    Ranking : 
        Your runtime beats 94.15 % of python3 submissions.
        Your memory usage beats 78.02 % of python3 submissions.
}
*/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''def reverse(arr: List[int], left: int, right: int):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        k %= len(nums)
        if k > 0:
            reverse(nums, 0, len(nums) - 1)
            reverse(nums, 0, k - 1)
            reverse(nums, k, len(nums) - 1)'''
        
        
        nlen = len(nums)
        k %= nlen
        out = nums[nlen-k:] + nums[:nlen-k]
        for i in range(nlen):
            nums[i] = out[i]
            
        
        