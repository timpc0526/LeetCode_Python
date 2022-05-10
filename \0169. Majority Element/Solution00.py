/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 62.95 %
    Runtime : 332 ms
    Memory Usage : 15.5 MB
    Testcase : 47 / 47 passed
    Ranking : 
        Your runtime beats 8.72 % of python3 submissions.
        Your memory usage beats 36.33 % of python3 submissions.
}
*/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #nums.sort()
        #print(nums)
        
        #226ms faster than 15.42
        '''appear = {}
        threshold = int(len(nums)/2)
        for i in nums:
            try:
                appear[i] = appear[i] + 1
            except:
                appear[i] = 0
            if appear[i] >= threshold:
                return i'''
        
        majority, count = None, 0
        for num in nums:
            if count == 0: majority = num
            count += 1 if num == majority else -1
        return majority
        