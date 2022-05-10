/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 41.62 %
    Runtime : 159 ms
    Memory Usage : 59.6 MB
    Testcase : 109 / 109 passed
    Ranking : 
        Your runtime beats 25.42 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import re
class Solution:
    def calculate(self, s: str) -> int:
        return int(eval("".join([char if char != '/' else '//' for char in s if char != ' '])))