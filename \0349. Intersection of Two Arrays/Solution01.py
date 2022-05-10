/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 69.10 %
    Runtime : 43 ms
    Memory Usage : 14.2 MB
    Testcase : 55 / 55 passed
    Ranking : 
        Your runtime beats 96.27 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
        