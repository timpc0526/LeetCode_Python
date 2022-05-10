/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 42.61 %
    Runtime : 195 ms
    Memory Usage : 14.2 MB
    Testcase : 20 / 20 passed
    Ranking : 
        Your runtime beats 5.03 % of python3 submissions.
        Your memory usage beats 96.20 % of python3 submissions.
}
*/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #tlen = len(tokens)
        num = []
        for i in tokens:
            if i == '+':
                c = num[-2:]
                num = num[:-2]
                num.append(sum(c))
            elif i == '-':
                c = num[-2:]
                num = num[:-2]
                num.append(c[0]-c[1])
            elif i == '*':
                c = num[-2:]
                num = num[:-2]
                num.append(c[0]*c[1])
            elif i == '/':
                c = num[-2:]
                num = num[:-2]
                num.append(int(c[0]/c[1]))
            else:
                num.append(int(i))
            #print(num)
        return num[0]