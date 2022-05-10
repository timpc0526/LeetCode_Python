/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 43.56 %
    Runtime : 28 ms
    Memory Usage : 14 MB
    Testcase : 104 / 104 passed
    Ranking : 
        Your runtime beats 97.97 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        self.bound = bound
        #xlist = [x**i for i in range(bound) if x**i <= bound]
        #ylist = [y**i for i in range(bound) if y**i <= bound]
        xlist, ylist = map(self.find, (x, y))
        return {i+j for i in xlist for j in ylist if i+j <= bound}
    
    
    def find(self, x):
        i = 0
        num = 0
        xlist = []
        if x == 1:
            return [x]
        while num <= self.bound:
            num = x**i
            xlist.append(num)
            i += 1
        return xlist
    
        
        
        
        # 49ms ft35.8
        '''def gen(base: int):
            curr = 1
            while curr <= bound:
                yield curr
                if base == 1: break
                curr *= base

        X, Y = map(list, map(gen, (x, y)))
        return {a + b for a in X for b in Y if a + b <= bound}'''
            
            