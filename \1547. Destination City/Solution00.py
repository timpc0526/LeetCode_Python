/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 77.70 %
    Runtime : 52 ms
    Memory Usage : 13.9 MB
    Testcase : 103 / 103 passed
    Ranking : 
        Your runtime beats 95.12 % of python3 submissions.
        Your memory usage beats 42.53 % of python3 submissions.
}
*/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        #
        A, B = map(set, zip(*paths))
        return (B - A).pop()
        
        