/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 60.89 %
    Runtime : 64 ms
    Memory Usage : 13.9 MB
    Testcase : 23 / 23 passed
    Ranking : 
        Your runtime beats 5.81 % of python3 submissions.
        Your memory usage beats 77.64 % of python3 submissions.
}
*/

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        llen = len(str(low))
        num = "123456789"
        out = []
        n, f = 0, 0
        while n < high:
            if f + llen >= 10:
                f = 0
                llen += 1
            n = int(num[f:f+llen])
            if low <= n <= high:
                out.append(n)
            f+=1
            if n == 123456789:
                break
        return out
        
        # 41ms ft53.31
        '''llen, f = len(str(low)), int(str(low)[0])-1
        num = "123456789"
        out = []
        n = 0
        while n < high:
            if f + llen >= 10:
                f = 0
                llen += 1
            n = int(num[f:f+llen])
            if low <= n <= high:
                out.append(n)
            f+=1
            if n == 123456789:
                break
        return out'''