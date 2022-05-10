/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 45.27 %
    Runtime : 43 ms
    Memory Usage : 13.9 MB
    Testcase : 232 / 232 passed
    Ranking : 
        Your runtime beats 60.89 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # 65ms ft21.2%
        biggest = float('-inf')
        bigger = float('-inf')
        for index, i in enumerate(nums):
            if i > biggest:
                bigger = biggest
                biggest = i
                pos = index
            elif i > bigger and i < biggest:
                bigger = i
        if biggest >= bigger*2:
            return pos
        else:
            return -1