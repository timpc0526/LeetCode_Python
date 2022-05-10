/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 83.41 %
    Runtime : 407 ms
    Memory Usage : 14.3 MB
    Testcase : 96 / 96 passed
    Ranking : 
        Your memory usage beats 5.88 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

from itertools import combinations
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        #n, total = len(arr), 0
        
        
        
        # 32ms ft97.14
        '''n, total = len(arr), 0
        for i, num in enumerate(arr):
            total += ((i + 1) * (n - i) + 1) // 2 * num
        return total'''
            
        
        allsum = 0
        arrlen = len(arr)
        for i in range(arrlen+1):
            if i%2 == 1:
                for j in range(arrlen):
                    if j+i > arrlen:
                        break
                    print(j)
                    print(j+i)
                    print(arr[j:j+i])
                    print("-------")
                    allsum += sum(arr[j:j+i])
        return allsum
                    
        