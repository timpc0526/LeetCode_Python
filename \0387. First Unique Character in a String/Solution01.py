/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 57.13 %
    Runtime : 119 ms
    Memory Usage : 14.1 MB
    Testcase : 104 / 104 passed
    Ranking : 
        Your runtime beats 74.10 % of python3 submissions.
        Your memory usage beats 96.49 % of python3 submissions.
}
*/

import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for index, i in enumerate(s):
            if count[i] == 1:
                return index
        return -1