/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 39.84 %
    Runtime : 271 ms
    Memory Usage : 15.2 MB
    Testcase : 74 / 74 passed
    Ranking : 
        Your runtime beats 24.89 % of python3 submissions.
        Your memory usage beats 88.36 % of python3 submissions.
}
*/


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        up, down, M = 0, 0, 0
        for i in range(1, len(A)):
            if down > 0 and A[i-1] < A[i] or A[i-1] == A[i]:
                up, down = 0, 0
            up += A[i-1] < A[i]
            down += A[i-1] > A[i]
            if up > 0 and down > 0:
                M = max(M, up + down + 1)
        return M
        
        '''minarr, maxarr = float('-inf'), float('-inf')
        alen = len(arr)
        top = 0
        bleft = 0
        bright = 0
        for i in range(1, alen-1):
            left = arr[i-1]
            mid = arr[i]
            right = arr[i+1]
            if mid > left and mid > right:
                top = i
                bleft = i-1
                bright = i+1
                for j in range(2, i+1):
                    if arr[i-j] < left:
                        left = arr[i-j]
                        bleft -= 1
                    else:
                        break
                for j in range(2, alen-i):
                    if arr[i+j] < right:
                        right = arr[i+j]
                        bright += 1
                    else:
                        break
        print(top)
        print(bright)
        print(bleft)
        if top == 0:
            return 0
        else:
            return bright-bleft+1'''
        
        