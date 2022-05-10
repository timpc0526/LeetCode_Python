/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 42.61 %
    Runtime : 113 ms
    Memory Usage : 14.4 MB
    Testcase : 20 / 20 passed
    Ranking : 
        Your runtime beats 29.50 % of python3 submissions.
        Your memory usage beats 18.44 % of python3 submissions.
}
*/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #tlen = len(tokens)
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda x, y: int(x / y),
        }
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                second, first = stack.pop(), stack.pop()
                stack.append(operators[token](first, second))
        return stack.pop()
        
        
        
        # 195ms ft5.05
        '''num = []
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
        return num[0]'''