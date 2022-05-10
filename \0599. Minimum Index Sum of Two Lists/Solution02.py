/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 52.75 %
    Runtime : 300 ms
    Memory Usage : 14.5 MB
    Testcase : 136 / 136 passed
    Ranking : 
        Your runtime beats 33.79 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minnum = float('inf')
        same = []
        for index_i, i in enumerate(list1):
            if i in list2:
                new = index_i+list2.index(i)
                if new < minnum:
                    minnum = new
                    same = [i]
                elif new == minnum:
                    same.append(i)
        return same