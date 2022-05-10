/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 42.85 %
    Runtime : 120 ms
    Memory Usage : 31 MB
    Testcase : 111 / 111 passed
    Ranking : 
        Your runtime beats 00.00 % of submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import numpy as np
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k = len(digits)
        digits[k-1] = digits[k-1]+1
        if digits[k-1] < 10:
            return digits
        for i in range(k-1,-1,-1):
            if digits[i] == 10:
                if i == 0:
                    digits = np.insert(digits,0,1)
                    digits[i+1] = 0
                else:
                    digits[i] = 0
                    digits[i-1] += 1
            else:
                break
        return digits