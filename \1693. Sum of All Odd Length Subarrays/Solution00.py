/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 83.41 %
    Runtime : 76 ms
    Memory Usage : 14.1 MB
    Testcase : 96 / 96 passed
    Ranking : 
        Your runtime beats 60.10 % of python3 submissions.
        Your memory usage beats 9.83 % of python3 submissions.
}
*/

from itertools import combinations
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        # 32ms ft97.14
        '''n, total = len(arr), 0
        for i, num in enumerate(arr):
            total += ((i + 1) * (n - i) + 1) // 2 * num
        return total'''
        
        # 60ms ft66.75
        allsum = 0
        arrlen = len(arr)
        for i in range(arrlen+1):
            if i%2 == 1:
                for j in range(arrlen):
                    if j+i > arrlen:
                        break
                    allsum += sum(arr[j:j+i])
        return allsum
                    
        