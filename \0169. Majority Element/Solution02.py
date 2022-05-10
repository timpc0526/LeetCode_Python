/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 62.95 %
    Runtime : 223 ms
    Memory Usage : 15.5 MB
    Testcase : 47 / 47 passed
    Ranking : 
        Your runtime beats 47.58 % of python3 submissions.
        Your memory usage beats 86.86 % of python3 submissions.
}
*/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #nums.sort()
        #print(nums)
        
        appear = {}
        threshold = int(len(nums)/2)
        #print("threshold: ",threshold)
        for i in nums:
            try:
                appear[i] = appear[i] + 1
            except:
                appear[i] = 0
            #print(appear[i])
            if appear[i] >= threshold:
                return i
        