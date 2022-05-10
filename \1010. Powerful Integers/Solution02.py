/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 43.56 %
    Runtime : 49 ms
    Memory Usage : 13.9 MB
    Testcase : 104 / 104 passed
    Ranking : 
        Your runtime beats 39.09 % of python3 submissions.
        Your memory usage beats 82.23 % of python3 submissions.
}
*/

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        def gen(base: int):
            curr = 1
            while curr <= bound:
                yield curr
                if base == 1: break
                curr *= base

        X, Y = map(list, map(gen, (x, y)))
        return {a + b for a in X for b in Y if a + b <= bound}
            
            