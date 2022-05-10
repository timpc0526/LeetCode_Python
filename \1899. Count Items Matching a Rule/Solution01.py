/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 84.39 %
    Runtime : 401 ms
    Memory Usage : 20.1 MB
    Testcase : 92 / 92 passed
    Ranking : 
        Your runtime beats 18.73 % of python3 submissions.
        Your memory usage beats 99.10 % of python3 submissions.
}
*/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key = None
        out = 0
        if ruleKey == "type":
            key = 0
        elif ruleKey == "color":
            key = 1
        elif ruleKey == "name":
            key = 2
        #print(*items[key])
        #num = *items[key].split(' ')
        for index, i in enumerate(zip(*items)):
            if index == key:
                for j in i:
                    if j == ruleValue:
                        out+=1
        return out
        