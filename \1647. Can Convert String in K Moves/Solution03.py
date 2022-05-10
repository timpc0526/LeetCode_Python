/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 32.53 %
    Runtime : 690 ms
    Memory Usage : 15.1 MB
    Testcase : 155 / 155 passed
    Ranking : 
        Your memory usage beats 87.50 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        
        if len(s) != len(t): return False
        counter = collections.Counter()
        for sc, tc in zip(s, t):
            shift = (ord(tc) - ord(sc)) % 26
            if shift > 0 and shift + counter[shift] * 26 > k: return False
            counter[shift] += 1
        return True
        
        '''if len(s) != len(t): return False
        #abc = 'abcdefghijklmnopqrstuvwxyz'
        out = 0
        a, b = [], []
        maxnum = 0
        for i, j in zip(s, t):
            if i != j:
                a.append(ord(i))
                b.append(ord(j))
                shift = (ord(j) - ord(i)) % 26
                print(shift)
        print((a,b))
        out = [max(maxnum, y-x) for x in a for y in b]
        print(out)'''
                
        