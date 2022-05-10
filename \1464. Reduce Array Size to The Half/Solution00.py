/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 68.36 %
    Runtime : 612 ms
    Memory Usage : 36.4 MB
    Testcase : 33 / 33 passed
    Ranking : 
        Your runtime beats 87.48 % of python3 submissions.
        Your memory usage beats 31.65 % of python3 submissions.
}
*/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        alen = len(arr)
        ans = 0
        c = collections.Counter(arr)
        for _, count in c.most_common():
            if alen <= len(arr) // 2: break
            alen -= count
            ans += 1
        return ans
        
        
        