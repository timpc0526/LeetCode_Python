/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 42.32 %
    Runtime : 48 ms
    Memory Usage : 14.8 MB
    Testcase : 62 / 62 passed
    Ranking : 
        Your runtime beats 94.16 % of python3 submissions.
        Your memory usage beats 6.91 % of python3 submissions.
}
*/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[len(nums)-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif target > nums[i] and target < nums[i+1]:
                return i+1
            