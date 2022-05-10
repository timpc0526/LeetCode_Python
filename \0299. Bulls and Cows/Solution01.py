/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 47.25 %
    Runtime : 66 ms
    Memory Usage : 14 MB
    Testcase : 152 / 152 passed
    Ranking : 
        Your runtime beats 33.59 % of python3 submissions.
        Your memory usage beats 31.77 % of python3 submissions.
}
*/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        x = y = 0
        s = [0] * 10
        g = [0] * 10
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                x += 1
            else:
                s[int(secret[i])] += 1
                g[int(guess[i])] += 1
        
        for i in range(10):
            y += min(s[i], g[i])
        
        return str(x) + "A" + str(y) + "B"
        
        
        # 121ms ft5.06
        '''A = 0
        B = 0
        temp_a = []
        temp_b = []
        for i, j in zip(secret, guess):
            if i == j:
                A += 1
            else:
                temp_a.append(i)
                temp_b.append(j)
        for i in temp_a:
            if i in temp_b:
                B+=1
                temp_b.remove(i)
        A, B = map(str, (A, B))
        return A+'A'+B+'B'''
                