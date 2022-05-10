/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 73.22 %
    Runtime : 32 ms
    Memory Usage : 14.1 MB
    Testcase : 100 / 100 passed
    Ranking : 
        Your runtime beats 83.72 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # 32ms ft70.07
        self.abc = "abcdefghijklmnopqrstuvwxyz"
        return (self.get_value(firstWord) + self.get_value(secondWord)) == self.get_value(targetWord)
        
    def get_value(self, Word):
        out = ""
        for i in Word:
            out += str(self.abc.find(i))
        return int(out)