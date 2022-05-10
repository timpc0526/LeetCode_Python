/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 65.05 %
    Runtime : 188 ms
    Memory Usage : 18.9 MB
    Testcase : 21 / 21 passed
    Ranking : 
        Your runtime beats 17.91 % of python3 submissions.
        Your memory usage beats 25.11 % of python3 submissions.
}
*/

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = Counter(nums)
        rank = []
        for index, key in enumerate(sorted(result.items(), key=lambda x:x[1], reverse=True)):
            if index < k:
                print(key[0] , " :: " , key[1])
                rank.append(key[0])
            else:
                return rank
        return rank
        