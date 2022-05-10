/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 68.00 %
    Runtime : 804 ms
    Memory Usage : 35.9 MB
    Testcase : 101 / 101 passed
    Ranking : 
        Your runtime beats 66.77 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import numpy as np
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
     
        # runtime error
        points.append((float(inf),float(inf)))
        ans = -1
        dis_func = lambda pos: abs(pos[0]-x)+abs(pos[1]-y)
        for index, i in enumerate(points):
            if (i[0] == x or i[1] == y) and (dis_func(i) < dis_func(points[ans])):
                ans = index
        return ans
                