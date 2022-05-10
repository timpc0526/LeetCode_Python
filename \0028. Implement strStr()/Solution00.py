/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 35.92 %
    Runtime : 24 ms
    Memory Usage : 14.6 MB
    Testcase : 80 / 80 passed
    Ranking : 
        Your runtime beats 98.80 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # 60ms
        '''h, n = len(haystack), len(needle)
        if n == 0: return 0
        if h < n: return -1
        i, next_ = 0, [0] * n
        for j in range(1, n):
            while i > 0 and needle[i] != needle[j]:
                i = next_[i - 1]
            i += needle[i] == needle[j]
            next_[j] = i
        i = 0
        for j in range(h):
            while i > 0 and needle[i] != haystack[j]:
                i = next_[i - 1]
            i += needle[i] == haystack[j]
            if i == n: return j - i + 1
        return -1'''
        
        ## 114ms
        '''n = len(needle)
        h = len(haystack)
        if needle not in haystack: return -1
        elif needle == haystack: return 0
        else:
            for i in range(h):
                if haystack[i:i+n] == needle:
                    return i'''
        
        ## 32ms
        '''if needle == "":
            return 0
        else:
            return haystack.find(needle)'''
            
        return haystack.find(needle)
        