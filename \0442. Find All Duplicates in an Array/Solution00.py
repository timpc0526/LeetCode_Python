/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 72.42 %
    Runtime : 356 ms
    Memory Usage : 22.6 MB
    Testcase : 28 / 28 passed
    Ranking : 
        Your runtime beats 93.73 % of python3 submissions.
        Your memory usage beats 24.76 % of python3 submissions.
}
*/

from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # 476ms ft39.69
        result = Counter(nums)
        out = []
        for i in result:
            if result[i] == 2:
                out.append(i)
        return out