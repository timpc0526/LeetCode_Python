/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 54.93 %
    Runtime : 60 ms
    Memory Usage : 13.9 MB
    Testcase : 56 / 56 passed
    Ranking : 
        Your runtime beats 65.53 % of python3 submissions.
        Your memory usage beats 85.92 % of python3 submissions.
}
*/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 68ms ft48.52
        out = []
        for i in nums1:
            if i in nums2:
                out.append(i)
                nums2.remove(i)
        return out
        