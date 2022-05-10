/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 59.47 %
    Runtime : 54 ms
    Memory Usage : 14.3 MB
    Testcase : 3999 / 3999 passed
    Ranking : 
        Your runtime beats 78.65 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for k in d:
            while num >= k:
                res += d[k]
                num -= k
        return res
        '''self.num_list = ["I", "V", "X", "L", "C", "D", "M"]
        self.num_list2 = [[0], [0,0], [0,0,0], [0,1], [1], [1, 0], [1, 0, 0], [1, 0, 0, 0], [0, 2], [2]]
        out = ""
        string = str(num)
        slen = len(string)
        for index, i in enumerate(range(slen, 0, -1)):
            #print(index)
            s = string[index]
            i = (i-1) *2
            if len(string) == 1:
                i = 0
            #print(i)
            #print(s)
            out += self.count(i, s)
        return out
    def count(self, leng, num):
        out = ""
        roman_list = self.num_list2[int(num)-1]
        print(roman_list)
        for i in roman_list:
            out += self.num_list[i+leng]
        return out'''
            
            