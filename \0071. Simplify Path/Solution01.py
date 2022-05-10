/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 38.83 %
    Runtime : 42 ms
    Memory Usage : 13.9 MB
    Testcase : 256 / 256 passed
    Ranking : 
        Your runtime beats 65.08 % of python3 submissions.
        Your memory usage beats 82.92 % of python3 submissions.
}
*/

class Solution:
    def simplifyPath(self, path: str) -> str:
        #dic = collections.defaultdict(self.zero)
        
        # 36ms ft76.19
        sp = path.split('/')
        slen = len(sp)
        out = []
        for index, i in enumerate(sp):
            if i =='.' or i == '':
                continue
            elif i == '..':
                out = out[:-1]
            else:
                out.append('/'+i)
        
        final = ''.join(out)
        if final == '': return '/'
        return final
    
        
                
                