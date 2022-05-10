/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 70.11 %
    Runtime : 114 ms
    Memory Usage : 14.2 MB
    Testcase : 15 / 15 passed
    Ranking : 
        Your runtime beats 22.75 % of python3 submissions.
        Your memory usage beats 57.72 % of python3 submissions.
}
*/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        '''for i, v in enumerate(nums1):
            equal = nums2.index(v)
            
            remainder = nums2[equal+1:]
            greater = -1
            
            for j, val in enumerate(remainder):
                if val > v:
                    greater = val
                    break
            
            nums1[i] = greater
              
        return nums1'''
        
        out = []
        n1, n2 = len(nums1), len(nums2)
        for i in range(n1):
            dex = int(nums2.index(nums1[i]))
            if dex == n2-1:
                out.append(-1)
                continue
            great = -1
            for j in nums2[dex:]: 
                if j > nums1[i]:
                    great = j
                    break
            out.append(great)
        return out