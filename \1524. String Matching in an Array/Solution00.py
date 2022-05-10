/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 63.86 %
    Runtime : 69 ms
    Memory Usage : 14 MB
    Testcase : 67 / 67 passed
    Ranking : 
        Your runtime beats 18.59 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # 47ms 68.83
        wlen = len(words)
        out = []
        for i in range(wlen):
            for j in range(wlen):
                if words[i] in words[j] and words[i] != words[j]:
                    out.append(words[i])
        return set(out)