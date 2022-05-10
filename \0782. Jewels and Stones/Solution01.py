/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 87.72 %
    Runtime : 54 ms
    Memory Usage : 14 MB
    Testcase : 255 / 255 passed
    Ranking : 
        Your runtime beats 23.37 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        out = 0
        for i in jewels:
            out+=stones.count(i)
        return out
        
        
        # 44ms ft44.92
        '''j = set(jewels)
        return sum(s in j for s in stones)'''
        
        # 44ms ft44.92
        '''out = 0
        for i in stones:
            if i in jewels:
                out += 1
        return out'''