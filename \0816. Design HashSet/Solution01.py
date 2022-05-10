/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 66.45 %
    Runtime : 148 ms
    Memory Usage : 18.9 MB
    Testcase : 32 / 32 passed
    Ranking : 
        Your runtime beats 97.80 % of python3 submissions.
        Your memory usage beats 55.91 % of python3 submissions.
}
*/

class MyHashSet:

    def __init__(self):
        self.hset = set()

    def add(self, key: int) -> None:
        self.hset.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hset.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.hset:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)