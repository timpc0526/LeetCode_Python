/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 42.41 %
    Runtime : 112 ms
    Memory Usage : 15.4 MB
    Testcase : 82 / 82 passed
    Ranking : 
        Your runtime beats 97.97 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #nums.sort()
        out = []
        nlen = len(nums)//3
        result = Counter(nums)
        for i in result:
            if result[i] > nlen:
                out.append(i)
        return out
        
        