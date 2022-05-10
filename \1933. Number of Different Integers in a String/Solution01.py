/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 35.67 %
    Runtime : 45 ms
    Memory Usage : 13.8 MB
    Testcase : 85 / 85 passed
    Ranking : 
        Your runtime beats 50.39 % of python3 submissions.
        Your memory usage beats 64.14 % of python3 submissions.
}
*/

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        digit = ""
        out = []
        for index, i in enumerate(word):
            if i.isdigit():
                digit += i
            else:
                digit += ' '
        for i in digit.split(' '):
            if i != '':
                out.append(int(i))
        out = set(out)
        return len(out)
            