/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 31.79 %
    Runtime : 1839 ms
    Memory Usage : 14.4 MB
    Testcase : 180 / 180 passed
    Ranking : 
        Your runtime beats 33.02 % of python3 submissions.
        Your memory usage beats 16.10 % of python3 submissions.
}
*/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen = len(s)
        start, end = 0, 0
        i, j = 0, 0
        while j < len(s):
            left, right = i, j
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left > end - start:
                    start, end = left, right
                left -= 1
                right += 1
            if i == j:
                j += 1
            else:
                i += 1
        return s[start:end+1]
        
        '''slen = len(s)
        print(slen)
        s2 = s*2
        print(s2)
        num = 0
        out = ""
        check = False
        for i in range(slen):
            if s2[i] == s2[-(i+1)]:
                print(s2[i])
                print(s2[-i])
                if check == True:
                    out+=s2[i]
                else:
                    out+=s2[i]
                    check = True
            else:
                if len(out) <1:
                    out = ""
                check = False
        if out == "":
            out = s[0]
        return out'''
                    
            
        