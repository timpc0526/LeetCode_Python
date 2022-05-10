/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 49.06 %
    Runtime : 42 ms
    Memory Usage : 14.2 MB
    Testcase : 301 / 301 passed
    Ranking : 
        Your runtime beats 78.05 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import re
#import numpy as np
class Solution:
    def secondHighest(self, s: str) -> int:
        
        # 32ms ft92.52
        pos = []
        for i in s:
            if i.isdigit():
                pos.append(int(i))
        pos = sorted(list(set(pos)))
        if len(pos) <= 1:
            return -1
        else:
            return pos[-2]
        
        