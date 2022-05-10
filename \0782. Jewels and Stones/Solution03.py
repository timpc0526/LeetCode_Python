/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 87.72 %
    Runtime : 45 ms
    Memory Usage : 13.9 MB
    Testcase : 255 / 255 passed
    Ranking : 
        Your runtime beats 44.66 % of python3 submissions.
        Your memory usage beats 60.58 % of python3 submissions.
}
*/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 44ms ft44.92
        out = 0
        for i in stones:
            if i in jewels:
                out += 1
        return out