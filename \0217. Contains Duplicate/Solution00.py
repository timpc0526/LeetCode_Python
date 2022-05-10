/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 60.83 %
    Runtime : 479 ms
    Memory Usage : 26 MB
    Testcase : 69 / 69 passed
    Ranking : 
        Your runtime beats 81.03 % of python3 submissions.
        Your memory usage beats 72.54 % of python3 submissions.
}
*/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 464ms ft69.92
        if len(nums) == len(list(set(nums))):
            return False
        else:
            return True