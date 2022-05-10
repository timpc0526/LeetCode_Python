/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 38.83 %
    Runtime : 36 ms
    Memory Usage : 14 MB
    Testcase : 256 / 256 passed
    Ranking : 
        Your runtime beats 83.83 % of python3 submissions.
        Your memory usage beats 42.40 % of python3 submissions.
}
*/

class Solution:
    def simplifyPath(self, path: str) -> str:
        #dic = collections.defaultdict(self.zero)
        
        sp = path.split('/')
        slen = len(sp)
        print(sp)
        out = []
        drop = 0
        for index, i in enumerate(sp):
            if drop == True and index == slen-1 or i =='.' or i == '':
                continue
            elif i == '..':
                out = out[:-1]
            else:
                out.append('/'+i)
        
        #out = out[drop:]
        final = ''.join(out)
        if final == '': return '/'
        return final
    
        
                
                