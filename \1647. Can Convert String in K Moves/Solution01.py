/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 32.53 %
    Runtime : 684 ms
    Memory Usage : 15.4 MB
    Testcase : 155 / 155 passed
    Ranking : 
        Your memory usage beats 40.91 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        
        # 512ms ft53.91
        '''if len(s) != len(t): return False
        c = collections.Counter()
        for sc, tc in zip(s, t):
            shift = (ord(tc) - ord(sc)) % 26
            print(shift)
            print(c[shift])
            print('--')
            if shift > 0 and shift + c[shift] * 26 > k: return False
            c[shift] += 1
        return True'''
        
        if len(s) != len(t): return False
        abc = 'abcdefghijklmnopqrstuvwxyz'
        c = collections.Counter()
        maxnum = 0
        for i, j in zip(s, t):
            if i != j:
                shift = (abc.index(j) - abc.index(i)) %26
                if shift + c[shift] * 26 > k: return False
                c[shift] += 1
        return True
                
        