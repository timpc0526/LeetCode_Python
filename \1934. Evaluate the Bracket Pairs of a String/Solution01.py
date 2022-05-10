/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 66.64 %
    Runtime : 1956 ms
    Memory Usage : 54.4 MB
    Testcase : 105 / 105 passed
    Ranking : 
        Your runtime beats 16.08 % of python3 submissions.
        Your memory usage beats 44.37 % of python3 submissions.
}
*/

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # 1118ms ft68.9
        kv = {}
        for i in knowledge:
            kv[i[0]] = i[1]
        
        dic = collections.Counter()
        slen = len(s)
        out = ''
        for i in range(slen):
            if s[i] == '(':
                dic[')'] = i+1
            elif s[i] in dic:
                key = s[dic[')']:i]
                if key in kv:
                    out+=kv[key]
                else:
                    out += '?'
                del dic[')']
            elif dic:
                continue
            elif not dic:
                out += s[i]
        return out
                
                
            