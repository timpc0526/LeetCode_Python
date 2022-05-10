/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 87.72 %
    Runtime : 44 ms
    Memory Usage : 13.8 MB
    Testcase : 255 / 255 passed
    Ranking : 
        Your runtime beats 47.67 % of python3 submissions.
        Your memory usage beats 60.58 % of python3 submissions.
}
*/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        return sum(s in j for s in stones)
        
        # 44ms ft44.92
        '''out = 0
        for i in stones:
            if i in jewels:
                out += 1
        return out'''