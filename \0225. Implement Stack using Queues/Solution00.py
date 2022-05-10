/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 55.24 %
    Runtime : 28 ms
    Memory Usage : 14 MB
    Testcase : 16 / 16 passed
    Ranking : 
        Your runtime beats 95.11 % of python3 submissions.
        Your memory usage beats 73.28 % of python3 submissions.
}
*/

class MyStack:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        return(self.s.pop())

    def top(self) -> int:
        return(self.s[-1])

    def empty(self) -> bool:
        if self.s == []:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()