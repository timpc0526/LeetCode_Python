/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 43.58 %
    Runtime : 93 ms
    Memory Usage : 14.5 MB
    Testcase : 129 / 129 passed
    Ranking : 
        Your runtime beats 54.39 % of python3 submissions.
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
        # 72ms ft56.78   
        sub = ""
        slen = len(s)
        for i in range(1, int(slen/2)+1):
            if slen % i == 0:
                sub = s[:i]
                re = s.replace(sub, '')
                if re == "":
                    return True
        return False

                        
        