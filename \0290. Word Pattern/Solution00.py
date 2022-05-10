/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 40.19 %
    Runtime : 28 ms
    Memory Usage : 13.9 MB
    Testcase : 36 / 36 passed
    Ranking : 
        Your runtime beats 93.42 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        sp = s.split(" ")

        if len(sp) != len(pattern):
            return False

        for i,x in enumerate(sp):
            d[pattern[i]] = x

        for i,x in enumerate(pattern):
            if x in d and d[x] != sp[i]:
                return False

        return len(set(sp)) == len(d.keys())
        
        
        
        #44ms ft49.68
        '''sl = s.split(' ')
        dic = {}
        same = []
        if len(sl) != len(pattern):
            return False
        for i, j in zip(pattern, sl):
            if i in dic.keys():
                if dic[i] != j:
                    return False
            else:
                if j in same:
                    return False
                dic[i] = j
                same.append(j)
        return True'''