/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 60.26 %
    Runtime : 102 ms
    Memory Usage : 14.3 MB
    Testcase : 141 / 141 passed
    Ranking : 
        Your runtime beats 00.00 % of submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        if '0' not in s:
            return True
        elif '1' not in s:
            return False
        zero = s.split('1')
        one = s.split('0')
        print(zero)
        print(one)
        maxone = 0
        maxzero = 0
        out = None
        for i in one:
            for j in zero:
                maxone = max(len(i), maxone)
                maxzero = max(len(j), maxzero)
        if maxone > maxzero:
            return True
        else:
            return False