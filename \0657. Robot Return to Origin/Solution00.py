/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 75.06 %
    Runtime : 91 ms
    Memory Usage : 14.2 MB
    Testcase : 75 / 75 passed
    Ranking : 
        Your runtime beats 32.01 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import itertools
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        #move = {'U':1, 'D':-1, 'R':1, 'L':-1}
        x = 0
        y = 0
        for k, g in itertools.groupby(sorted(moves)):
            g = list(g)
            glen = len(g)
            if k in 'UD':
                if k == 'U':
                    x+=glen
                else:
                    x-=glen
            else:
                if k == 'R':
                    y+=glen
                else:
                    y-=glen
        if (x, y) == (0,0):
            return True
        else:
            return False
        