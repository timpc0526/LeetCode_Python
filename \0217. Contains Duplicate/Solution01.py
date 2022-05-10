/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 60.83 %
    Runtime : 464 ms
    Memory Usage : 26 MB
    Testcase : 69 / 69 passed
    Ranking : 
        Your runtime beats 89.80 % of python3 submissions.
        Your memory usage beats 30.36 % of python3 submissions.
}
*/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(list(set(nums))):
            return False
        else:
            return True