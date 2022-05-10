/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 81.40 %
    Runtime : 28 ms
    Memory Usage : 13.9 MB
    Testcase : 79 / 79 passed
    Ranking : 
        Your runtime beats 95.51 % of python3 submissions.
        Your memory usage beats 56.76 % of python3 submissions.
}
*/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
        
        