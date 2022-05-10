/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 57.13 %
    Runtime : 92 ms
    Memory Usage : 14.3 MB
    Testcase : 104 / 104 passed
    Ranking : 
        Your runtime beats 91.50 % of python3 submissions.
        Your memory usage beats 19.98 % of python3 submissions.
}
*/

import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        #119ms ft75.48
        count = collections.Counter(s)
        for index, i in enumerate(s):
            if count[i] == 1:
                return index
        return -1