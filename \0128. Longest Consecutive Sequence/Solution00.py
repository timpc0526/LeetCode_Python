/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 48.70 %
    Runtime : 336 ms
    Memory Usage : 23.4 MB
    Testcase : 70 / 70 passed
    Ranking : 
        Your runtime beats 52.50 % of python3 submissions.
        Your memory usage beats 91.51 % of python3 submissions.
}
*/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        nlen = len(nums)
        if nlen == 0: return 0
        maxnum = 0
        count = 1
        for i in range(1, nlen):
            if nums[i] - nums[i-1] == 1:
                count += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                maxnum = max(maxnum, count)
                count = 1
        return max(maxnum, count)