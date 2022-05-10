/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 49.06 %
    Runtime : 54 ms
    Memory Usage : 14.4 MB
    Testcase : 301 / 301 passed
    Ranking : 
        Your runtime beats 47.38 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import re
#import numpy as np
class Solution:
    def secondHighest(self, s: str) -> int:
        pos = []
        for i in s:
            if i.isdigit():
                pos.append(int(i))
        print(pos)
        pos = sorted(list(set(pos)))
        if len(pos) <= 1:
            return -1
        else:
            return pos[-2]
        
        