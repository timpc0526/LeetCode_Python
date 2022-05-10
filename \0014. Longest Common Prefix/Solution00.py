/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 39.45 %
    Runtime : 32 ms
    Memory Usage : 14.3 MB
    Testcase : 123 / 123 passed
    Ranking : 
        Your runtime beats 94.25 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        last = '' if not strs else strs.pop()
        for i, c in enumerate(last):
            for s in strs:
                if i >= len(s) or s[i] != c:
                    return last[:i]
        return last
    
        '''str_list = []
        str_dict = {}
        for i in range()
        for s in strs:
            for index, j in enumerate(list(s)):
                if str_dict[index] == None:
                str_dict[index] = j
                
        for i in range(len(strs)):
            print(list(strs[i]))
            str_list.append(list(strs[i])) 
        print(str_list)
        return 0'''
    