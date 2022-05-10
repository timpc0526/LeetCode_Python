/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 52.64 %
    Runtime : 209 ms
    Memory Usage : 19.2 MB
    Testcase : 87 / 87 passed
    Ranking : 
        Your runtime beats 69.28 % of python3 submissions.
        Your memory usage beats 10.46 % of python3 submissions.
}
*/

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # 206ms ft71.3
        dic = collections.defaultdict(self.zero)
        for row in wall:
            for i in range(len(row)-1):
                dic[row[i]] += 1
                row[i+1] += row[i]
        return len(wall) - max(dic.values(), default= 0)
    def zero(self):
        return 0
        
        
        # 196ms ft68.83
        '''counter = collections.Counter()
        for row in wall:
            for i in range(len(row) - 1):
                counter[row[i]] += 1
                row[i+1] += row[i]
        return len(wall) - max(counter.values(), default=0)'''
        