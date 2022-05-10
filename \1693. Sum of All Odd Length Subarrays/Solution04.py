/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 83.41 %
    Runtime : 32 ms
    Memory Usage : 14.2 MB
    Testcase : 96 / 96 passed
    Ranking : 
        Your runtime beats 99.57 % of python3 submissions.
        Your memory usage beats 6.23 % of python3 submissions.
}
*/

from itertools import combinations
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n, total = len(arr), 0
        for i, num in enumerate(arr):
            total += ((i + 1) * (n - i) + 1) // 2 * num
        return total
        
        
        '''allsum = 0
        arrlen = len(arr)
        for i in range(arrlen+1):
            if i%2 == 1:
                
                temp = combinations(arr, i)
                for j in list(temp):
                    print(j)
                    allsum += sum(j)
        return allsum'''
                    
        