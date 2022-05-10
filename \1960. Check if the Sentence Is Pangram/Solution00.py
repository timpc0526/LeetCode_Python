/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 81.40 %
    Runtime : 46 ms
    Memory Usage : 13.8 MB
    Testcase : 79 / 79 passed
    Ranking : 
        Your runtime beats 42.14 % of python3 submissions.
        Your memory usage beats 95.94 % of python3 submissions.
}
*/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # 28ms ft92.78
        return len(set(sentence)) == 26
        
        