/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 62.95 %
    Runtime : 226 ms
    Memory Usage : 15.6 MB
    Testcase : 47 / 47 passed
    Ranking : 
        Your runtime beats 45.89 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #nums.sort()
        #print(nums)
        
        appear = {}
        threshold = int(len(nums)/2)
        for i in nums:
            try:
                appear[i] = appear[i] + 1
            except:
                appear[i] = 0
            if appear[i] >= threshold:
                return i
        