/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 52.64 %
    Runtime : 262 ms
    Memory Usage : 18.9 MB
    Testcase : 87 / 87 passed
    Ranking : 
        Your runtime beats 39.00 % of python3 submissions.
        Your memory usage beats 93.46 % of python3 submissions.
}
*/

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        
        counter = collections.Counter()
        for row in wall:
            for i in range(len(row) - 1):
                counter[row[i]] += 1
                row[i+1] += row[i]
        return len(wall) - max(counter.values(), default=0)
        