/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 69.65 %
    Runtime : 69 ms
    Memory Usage : 14.4 MB
    Testcase : 105 / 105 passed
    Ranking : 
        Your runtime beats 24.26 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # 70ms ft10.35
        arr.sort()
        arrlen= len(arr)
        dis = arr[1] - arr[0]
        for i in range(1, arrlen):
            if (arr[i] - arr[i-1]) != dis:
                return False
        return True
        
        '''arr.sort()
        arr2 = [a-arr[0] for a in arr]
        for i in arr2:
            if i%arr[0] != 0:
                return False
        return True'''
        
        
        '''arr.sort()
        arrmax = arr[-1]
        arrmin = arr[0]
        arrlen = len(arr)
        print(arrmax)
        print(arrmin)
        step = (arrmax-arrmin)/(arrlen-1)
        print(step)
        try:
            corarr = list(range(arrmin, arrmax+1, int(step)))
            print(corarr)
            print(arr)
            if arr == corarr:
                return True
            return False
        except:
            return False'''
        