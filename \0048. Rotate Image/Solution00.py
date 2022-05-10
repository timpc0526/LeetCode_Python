/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 66.70 %
    Runtime : 32 ms
    Memory Usage : 13.9 MB
    Testcase : 21 / 21 passed
    Ranking : 
        Your runtime beats 95.81 % of python3 submissions.
        Your memory usage beats 75.66 % of python3 submissions.
}
*/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for index, i in enumerate(zip(*matrix)):
            matrix[index] = i[::-1]