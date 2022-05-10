/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 28.29 %
    Runtime : 52 ms
    Memory Usage : 13.9 MB
    Testcase : 45 / 45 passed
    Ranking : 
        Your runtime beats 28.57 % of python3 submissions.
        Your memory usage beats 73.33 % of python3 submissions.
}
*/

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        i, size = 0, 0
        while size < K:
            if S[i].isdigit():
                size *= int(S[i])
            else:
                size += 1
            i += 1
        for j in reversed(range(i)):
            K %= size
            if S[j].isdigit():
                size //= int(S[j])
            elif K == 0:
                return S[j]
            else:
                size -= 1
        
        
        
        # Memory Limit Exceeded	
        '''slen = len(s)
        new = ""
        for i in range(slen):
            if s[i].isdigit():
                num = int(s[i])
                new *= num
                if k < len(new):
                    return new[k-1]
            else:
                new += s[i]      
        return new[k-1]'''
                
                
        