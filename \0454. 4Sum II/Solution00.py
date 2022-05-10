/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 57.07 %
    Runtime : 788 ms
    Memory Usage : 14.2 MB
    Testcase : 132 / 132 passed
    Ranking : 
        Your runtime beats 61.30 % of python3 submissions.
        Your memory usage beats 74.33 % of python3 submissions.
}
*/

#import itertools
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        counter = collections.Counter(a + b for a in nums1 for b in nums2)
        return sum(counter[-c - d] for c in nums3 for d in nums4)
        
        
        # time limit exceeded
        '''out = 0
        result = itertools.product(nums1, nums2, nums3, nums4)
        for i in result:
            if sum(i) == 0:
                out+=1
        return out'''