/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 64.23 %
    Runtime : 3600 ms
    Memory Usage : 17.7 MB
    Testcase : 115 / 115 passed
    Ranking : 
        Your memory usage beats 65.83 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # 5073ms ft5.01
        slen = len(strs)
        dic = []
        c = True
        for i in range(slen):
            sl = sorted(strs[i])
            if dic == []:
                dic.append([sl, strs[i]])
                continue
            for j in range(len(dic)):
                if sl in dic[j]:
                    dic[j].append(strs[i])
                    c = False
                    break
            if c:
                dic.append([sl, strs[i]])
            c = True
        for i in range(len(dic)):
            dic[i] = dic[i][1:]
        return dic
            
        
        