/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 42.61 %
    Runtime : 192 ms
    Memory Usage : 14.4 MB
    Testcase : 20 / 20 passed
    Ranking : 
        Your runtime beats 5.03 % of python3 submissions.
        Your memory usage beats 58.50 % of python3 submissions.
}
*/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tlen = len(tokens)
        #tokens = list(map(int, tokens))
        #print(tokens)
        dic1 = ['+', '-']
        dic2 = ['*', '/']
        num = []
        for i in range(tlen):
            if tokens[i] == '+':
                c = num[-2:]
                num = num[:-2]
                num.append(sum(c))
            elif tokens[i] == '-':
                c = num[-2:]
                num = num[:-2]
                num.append(c[0]-c[1])
            elif tokens[i] == '*':
                c = num[-2:]
                num = num[:-2]
                num.append(c[0]*c[1])
            elif tokens[i] == '/':
                c = num[-2:]
                num = num[:-2]
                num.append(int(c[0]/c[1]))
            else:
                num.append(int(tokens[i]))
            #print(num)
        return num[0]