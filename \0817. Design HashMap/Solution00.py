/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 65.27 %
    Runtime : 200 ms
    Memory Usage : 17.2 MB
    Testcase : 36 / 36 passed
    Ranking : 
        Your runtime beats 98.68 % of python3 submissions.
        Your memory usage beats 62.88 % of python3 submissions.
}
*/

class MyHashMap:

    def __init__(self):
        self.hset = {}

    def put(self, key: int, value: int) -> None:
        self.hset[key] = value

    def get(self, key: int) -> int:
        if key not in self.hset:
            return -1
        else:
            return self.hset[key]

    def remove(self, key: int) -> None:
        if key in self.hset:
            self.hset.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)