/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 65.66 %
    Runtime : 816 ms
    Memory Usage : 16.3 MB
    Testcase : 206 / 206 passed
    Ranking : 
        Your runtime beats 92.89 % of python3 submissions.
        Your memory usage beats 38.67 % of python3 submissions.
}
*/

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType)//2, len(set(candyType)))