/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 43.90 %
    Runtime : 41 ms
    Memory Usage : 13.9 MB
    Testcase : 59 / 59 passed
    Ranking : 
        Your runtime beats 74.58 % of python3 submissions.
        Your memory usage beats 86.65 % of python3 submissions.
}
*/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        for index, i in enumerate(sorted(nums1)):
            nums1[index] = i
        
        
        