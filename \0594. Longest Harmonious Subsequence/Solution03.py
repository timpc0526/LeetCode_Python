/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 52.70 %
    Runtime : 9108 ms
    Memory Usage : 16 MB
    Testcase : 206 / 206 passed
    Ranking : 
        Your memory usage beats 27.41 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        snums = sorted(list(set(nums)))
        dic = dict((i, nums.count(i)) for i in snums)
        maxnum = 0
        for i in range(1, len(snums)):
            if snums[i-1]-snums[i] == -1:
                maxnum = max(maxnum, dic[snums[i-1]]+dic[snums[i]])
        return maxnum