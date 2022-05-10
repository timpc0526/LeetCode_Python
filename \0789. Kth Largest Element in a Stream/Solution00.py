/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 54.79 %
    Runtime : 190 ms
    Memory Usage : 18 MB
    Testcase : 10 / 10 passed
    Ranking : 
        Your runtime beats 28.68 % of python3 submissions.
        Your memory usage beats 99.12 % of python3 submissions.
}
*/

import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        
        # 110ms ft66.7
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
            
        print(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
    
    
    # 1644ms ft6.94
    '''def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.n = nums
        
    def add(self, val: int) -> int:
        self.n.append(val)
        self.n = sorted(self.n)
        return self.n[-self.k]'''


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)