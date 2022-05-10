/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 62.11 %
    Runtime : 8213 ms
    Memory Usage : 15.7 MB
    Testcase : 223 / 223 passed
    Ranking : 
        Your memory usage beats 43.54 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nlen = len(nums)
        out = []
        for i in range(nlen):
            check = True
            for j in nums[i+1:]+nums[:i]:
                if j > nums[i]:
                    out.append(j)
                    check = False
                    break
            if check:
                out.append(-1)
        return out
        
        '''nlen = len(nums)
        dic = {}
        out = []
        for i in range(nlen-1):
            if nums[i] not in dic and nums[i] not in dic.values():
                dic[nums[i]] = nums[i+1]
        for i in nums:
            if i in dic:
                out.append(dic[i])
            else:
                out.append(-1)
        return out'''
                
            