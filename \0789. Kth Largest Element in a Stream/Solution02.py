/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 54.79 %
    Runtime : 1644 ms
    Memory Usage : 18.6 MB
    Testcase : 10 / 10 passed
    Ranking : 
        Your runtime beats 9.56 % of python3 submissions.
        Your memory usage beats 6.58 % of python3 submissions.
}
*/

class KthLargest:
    
    # 2019ms ft5.3
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.n = nums
        
    def add(self, val: int) -> int:
        self.n.append(val)
        self.n = sorted(self.n)
        return self.n[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)