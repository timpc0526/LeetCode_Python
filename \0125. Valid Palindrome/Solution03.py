/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 41.73 %
    Runtime : 36 ms
    Memory Usage : 14.8 MB
    Testcase : 480 / 480 passed
    Ranking : 
        Your runtime beats 98.72 % of python3 submissions.
        Your memory usage beats 33.45 % of python3 submissions.
}
*/

import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation)).replace(' ','').lower()
        '''s = s.replace(' ', '').replace(',','').replace(':','').replace('.','').replace('@','').replace('#','').lower()'''
        if len(s)%2 == 0:
            k = len(s)//2
            print(s[k:][::-1])
            print(s[:k])
            if s[k:][::-1] == s[:k]:
                return True
            else:
                return False
        if len(s)%2 == 1:
            k = (len(s)-1)//2
            print(s[k+1:][::-1])
            print(s[:k])
            if s[k+1:][::-1] == s[:k]:
                return True
            else:
                return False