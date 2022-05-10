/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 42.32 %
    Runtime : 48 ms
    Memory Usage : 15.1 MB
    Testcase : 62 / 62 passed
    Ranking : 
        Your runtime beats 94.16 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k = len(nums)
        if target > nums[k-1]:
            return k
        elif target < nums[0]:
            return 0
        for i in range(k):
            if target == nums[i]:
                return i
            elif target > nums[i] and target < nums[i+1]:
                return i+1
            