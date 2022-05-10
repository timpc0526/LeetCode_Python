/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 40.19 %
    Runtime : 44 ms
    Memory Usage : 13.9 MB
    Testcase : 36 / 36 passed
    Ranking : 
        Your runtime beats 41.58 % of python3 submissions.
        Your memory usage beats 75.00 % of python3 submissions.
}
*/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #61ms ft9.03
        sl = s.split(' ')
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
        return True