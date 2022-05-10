/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 63.86 %
    Runtime : 47 ms
    Memory Usage : 13.9 MB
    Testcase : 67 / 67 passed
    Ranking : 
        Your runtime beats 63.72 % of python3 submissions.
        Your memory usage beats 64.17 % of python3 submissions.
}
*/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        wlen = len(words)
        out = []
        for i in range(wlen):
            for j in range(wlen):
                if words[i] in words[j] and words[i] != words[j]:
                    out.append(words[i])
        return set(out)