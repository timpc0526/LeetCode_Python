/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 62.95 %
    Runtime : 371 ms
    Memory Usage : 15.6 MB
    Testcase : 47 / 47 passed
    Ranking : 
        Your runtime beats 00.00 % of submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #nums.sort()
        #print(nums)
        
        appear = {}
        threshold = int(len(nums)/2)
        print("threshold: ",threshold)
        for i in nums:
            try:
                appear[i] = appear[i] + 1
            except:
                appear[i] = 0
            print(appear[i])
            if appear[i] >= threshold:
                return i
        