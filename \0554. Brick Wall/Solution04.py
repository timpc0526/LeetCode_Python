/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 52.64 %
    Runtime : 196 ms
    Memory Usage : 18.9 MB
    Testcase : 87 / 87 passed
    Ranking : 
        Your runtime beats 80.17 % of python3 submissions.
        Your memory usage beats 61.44 % of python3 submissions.
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
        
        
        '''num = sum(wall[0])
        edge = []
        for i in (wall):
            a = 0
            temp = []
            for j in i:
                a += j
                temp.append(a)
            edge.append(temp)
        #print(edge)
        out = []
        for i in range(1, num+1):
            u = 0
            for j in edge:
                print(i)
                if i not in j or i == num:
                    u+=1
            out.append(u)
        #print(out)
        return min(out)'''
        
            