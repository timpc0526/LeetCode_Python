/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 48.69 %
    Runtime : 84 ms
    Memory Usage : 14.3 MB
    Testcase : 30 / 30 passed
    Ranking : 
        Your runtime beats 19.28 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import itertools
class Solution:
    def countAndSay(self, n: int) -> str:
        t = '1'
        for i in range(n-1):
            t = self.count(t)
        return t
    
    def count(self, t):
        out = ''
        for k, v in itertools.groupby(t):
            count = str(len(list(v)))
            out += (count+k)
        return out
        
    # 67ms ft31.8
        '''s = '1'
        for _ in range(n - 1):
            s = ''.join(str(sum(map(bool, v))) + k
                        for k, v in itertools.groupby(s))
            #print(s)
        return s'''
        
        
        
        '''num = "1"
        for i in range(n):
            #self.count(i)
            num = self.say(num)
            print(num)
            print("------")
        return num
    def count(self, s):
        print("hihi: ",s)
    def say(self, s):
        slen = len(s)
        if slen == 1:
            return "1"+s
        if slen == 2:
            return "2"+s[0]
        out = ""
        step = 0
        for i in range(1, slen):
            if s[i-1] != s[i]:
                out+=str(i-1-step)
                out+=s[i-1]
                step = i-1
                print(out)
        
        #print(out)
        return out'''
        
        
        