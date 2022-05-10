/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 77.65 %
    Runtime : 42 ms
    Memory Usage : 14.2 MB
    Testcase : 203 / 203 passed
    Ranking : 
        Your runtime beats 51.27 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x, y = coordinates[0], coordinates[1]
        string = "abcdefgh"
        #out1 = int(y)%2
        #out2 = string.find(x)%2+1
        return int(y)%2 == string.find(x)%2
            
            
            
        
        