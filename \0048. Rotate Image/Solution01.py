/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 66.70 %
    Runtime : 46 ms
    Memory Usage : 14 MB
    Testcase : 21 / 21 passed
    Ranking : 
        Your runtime beats 56.68 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        out = []
        for index, i in enumerate(zip(*matrix)):
            matrix[index] = i[::-1]