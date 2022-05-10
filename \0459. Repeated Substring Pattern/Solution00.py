/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 43.58 %
    Runtime : 46 ms
    Memory Usage : 14.4 MB
    Testcase : 129 / 129 passed
    Ranking : 
        Your runtime beats 84.44 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 72ms ft56.78   
        '''sub = ""
        slen = len(s)
        for i in range(1, int(slen/2)+1):
            if slen % i == 0:
                sub = s[:i]
                re = s.replace(sub, '')
                if re == "":
                    return True
        return False'''
        #44ms ft76.51
        return s in (2 * s)[1:-1]

                        
        