/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 61.25 %
    Runtime : 32 ms
    Memory Usage : 13.9 MB
    Testcase : 136 / 136 passed
    Ranking : 
        Your runtime beats 91.52 % of python3 submissions.
        Your memory usage beats 17.58 % of python3 submissions.
}
*/

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        cur = 1
        max_num = pow(10, 9)+1
        s = Counter(str(n))  # convert '112344' into  {1:2, 2:1, 3:1, 4:2}
        while cur < max_num:
            if Counter(str(cur)) == s:  # check if dict is same
                return True
            cur *=2
        return False