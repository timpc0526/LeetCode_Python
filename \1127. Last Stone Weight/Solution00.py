/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 64.38 %
    Runtime : 66 ms
    Memory Usage : 14 MB
    Testcase : 70 / 70 passed
    Ranking : 
        Your runtime beats 8.68 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 43ms ft49.66
        olen = len(stones)
        stones = [-i for i in stones]
        heapq.heapify(stones)
        for i in range(olen):
            if len(stones) >= 2:
                x = heapq.heappop(stones)
                y = heapq.heappop(stones)
            elif len(stones) == 1:
                return -stones[0]
            elif stones == []:
                if x != y:
                    return abs(x-y)
                else:
                    return 0
            if x != y:
                heapq.heappush(stones, x - y)