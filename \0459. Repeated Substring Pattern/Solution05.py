/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 43.58 %
    Runtime : 7333 ms
    Memory Usage : 14.6 MB
    Testcase : 129 / 129 passed
    Ranking : 
        Your runtime beats 00.00 % of submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''slen = len(s)
        for i in range(slen/2):
            for j in range(0, slen, i):
                if s[j:j+i] == s[j+i:j+2*i]:
                    return True
            return True'''
        
        '''sub = ""
        slen = len(s)
        for i in range(slen):
            print(s[i:i+len(sub)])
            if sub == s[i:i+len(sub)]:
                sub+=s[i]
            else:
                correct = None
                print("#####")
                print(i)
                for j in range(0, slen, i):
                    print(sub)
                    print(s[j:j+i])
                    print("-------")
                    if sub != s[j:j+i]:
                        return False
                return True'''
            
        sub = ""
        slen = len(s)
        for i in range(int(slen/2)):
            sub+=s[i]
            re = s.replace(sub, '')
            if re == "":
                return True
        return False

                        
        