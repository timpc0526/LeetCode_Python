/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 41.62 %
    Runtime : 169 ms
    Memory Usage : 59.5 MB
    Testcase : 109 / 109 passed
    Ranking : 
        Your runtime beats 21.06 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import re
class Solution:
    def calculate(self, s: str) -> int:
        return int(eval("".join([char if char != '/' else '//' for char in s if char != ' '])))