/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 35.92 %
    Runtime : 114 ms
    Memory Usage : 14.6 MB
    Testcase : 80 / 80 passed
    Ranking : 
        Your runtime beats 20.28 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        ## 156ms
        nee_len = len(needle)
        if needle not in haystack:
            return -1
        elif needle == haystack:
            return 0
        else:
            for i in range(len(haystack)):
                if haystack[i:i+nee_len] == needle:
                    return i
            
        