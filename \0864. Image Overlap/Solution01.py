/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 61.23 %
    Runtime : 499 ms
    Memory Usage : 56.8 MB
    Testcase : 59 / 59 passed
    Ranking : 
        Your runtime beats 00.00 % of submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        m, n = len(img1), len(img2)
        l1, l2 = [], []
        for i in range(m):
            for j in range(n):
                if img2[i][j] == 1:
                    l2.append((i, j))
                if img1[i][j] == 1:
                    l1.append((i, j))
        out = []
        for l2x, l2y in l2:
            for l1x, l1y in l1:
                out.append((l1x-l2x, l1y-l2y))

        counter = collections.Counter(out)
        return max(counter.values(), default=0)
        
        
