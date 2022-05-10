/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 54.37 %
    Runtime : 100 ms
    Memory Usage : 13.9 MB
    Testcase : 110 / 110 passed
    Ranking : 
        Your runtime beats 19.70 % of python3 submissions.
        Your memory usage beats 66.27 % of python3 submissions.
}
*/

import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [i[0] for i in heapq.nsmallest(k, collections.Counter(words).items(), key=lambda x: (-x[1], x[0]))]