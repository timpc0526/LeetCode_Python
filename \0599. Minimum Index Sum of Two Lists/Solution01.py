/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 52.75 %
    Runtime : 332 ms
    Memory Usage : 14.4 MB
    Testcase : 136 / 136 passed
    Ranking : 
        Your runtime beats 27.75 % of python3 submissions.
        Your memory usage beats 88.82 % of python3 submissions.
}
*/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        # 300ms ft32.82
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