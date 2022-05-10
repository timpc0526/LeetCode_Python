/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 50.27 %
    Runtime : 708 ms
    Memory Usage : 18.6 MB
    Testcase : 31 / 31 passed
    Ranking : 
        Your runtime beats 19.62 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        #self.s = sorted(self.s, reverse=True)
        #print(self.s)
        
    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        print(self.s)
        return(self.s[-1])

    def getMin(self) -> int:
        return(min(self.s))


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()