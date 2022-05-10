/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 57.87 %
    Runtime : 52 ms
    Memory Usage : 14.3 MB
    Testcase : 3999 / 3999 passed
    Ranking : 
        Your runtime beats 80.28 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def romanToInt(self, s: str) -> int:
        s = list(s)
        num = 0
        tmp1 = 0
        tmp2 = 0
        tmp_value = 0
        num_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i in range(len(s)):
            if i < len(s)-1 and num_dict[s[i]] < num_dict[s[i+1]]:
                num -= num_dict[s[i]]
            else:
                num += num_dict[s[i]]
        return num