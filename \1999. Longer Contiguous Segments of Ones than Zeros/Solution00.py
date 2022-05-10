/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 60.26 %
    Runtime : 51 ms
    Memory Usage : 14.3 MB
    Testcase : 141 / 141 passed
    Ranking : 
        Your runtime beats 32.47 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zeros, ones = 0, 0
        max_zeros, max_ones = 0, 0
        for c in s:
            if c == '0':
                zeros += 1
                ones = 0
                max_zeros = max(max_zeros, zeros)
            else:
                zeros = 0
                ones += 1
                max_ones = max(max_ones, ones)
        return max_ones > max_zeros
        
        
        # 84ms ft5.4
        '''if '0' not in s:
            return True
        elif '1' not in s:
            return False
        zero = s.split('1')
        one = s.split('0')
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
            return False'''