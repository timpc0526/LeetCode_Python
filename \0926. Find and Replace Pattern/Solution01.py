/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 75.58 %
    Runtime : 36 ms
    Memory Usage : 13.9 MB
    Testcase : 47 / 47 passed
    Ranking : 
        Your runtime beats 84.31 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        dic = collections.defaultdict(list)
        dic2 = collections.defaultdict(list)
        out = []
        for index, i in enumerate(pattern):
            dic[i].append(index)
        palist = list(dic.values())
        for w in words:
            for index, i in enumerate(w):
                dic2[i].append(index)
            
            if palist == list(dic2.values()):
                out.append(w)
            dic2 = collections.defaultdict(list)
        return out
        
        