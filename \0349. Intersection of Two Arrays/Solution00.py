/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 69.10 %
    Runtime : 63 ms
    Memory Usage : 14 MB
    Testcase : 55 / 55 passed
    Ranking : 
        Your runtime beats 57.49 % of python3 submissions.
        Your memory usage beats 69.11 % of python3 submissions.
}
*/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 43ms ft90.22
        return list(set(nums1) & set(nums2))
        