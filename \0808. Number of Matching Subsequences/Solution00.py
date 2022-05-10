/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 50.53 %
    Runtime : 412 ms
    Memory Usage : 15.8 MB
    Testcase : 52 / 52 passed
    Ranking : 
        Your runtime beats 91.01 % of python3 submissions.
        Your memory usage beats 32.83 % of python3 submissions.
}
*/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        nexts = collections.defaultdict(list)
        for I in map(iter, words):
            nexts[next(I)].append(I)
        for c in s:
            for I in nexts.pop(c, iter(())):
                nexts[next(I, None)].append(I)
        return len(nexts[None])
        
        '''out = 0
        s = collections.Counter(s)
        for i in words:
            w = collections.Counter(i)
            check = True
            for j in w:
                if s[j] < w[j]:
                    check = False
                    break
            if check:
                out+=1
        return out'''
        