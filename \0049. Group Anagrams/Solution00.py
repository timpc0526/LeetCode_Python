/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 64.23 %
    Runtime : 143 ms
    Memory Usage : 17.7 MB
    Testcase : 115 / 115 passed
    Ranking : 
        Your runtime beats 47.31 % of python3 submissions.
        Your memory usage beats 71.69 % of python3 submissions.
}
*/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # 103ms ft79.54
        slen = len(strs)
        dic = collections.defaultdict(list)
        for i in range(slen):
            sl = ''.join(sorted(strs[i]))
            dic[sl].append(strs[i])
        return (dic.values())
        
        
        # 3600ms ft5.01
        '''slen = len(strs)
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
        return dic'''
            
        
        