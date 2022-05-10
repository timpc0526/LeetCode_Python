/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 54.93 %
    Runtime : 68 ms
    Memory Usage : 13.8 MB
    Testcase : 56 / 56 passed
    Ranking : 
        Your runtime beats 51.94 % of python3 submissions.
        Your memory usage beats 99.02 % of python3 submissions.
}
*/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        for i in nums1:
            if i in nums2:
                out.append(i)
                nums2.remove(i)
        return out
        