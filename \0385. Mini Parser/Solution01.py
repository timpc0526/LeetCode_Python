/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 35.89 %
    Runtime : 109 ms
    Memory Usage : 17.4 MB
    Testcase : 58 / 58 passed
    Ranking : 
        Your runtime beats 30.73 % of python3 submissions.
        Your memory usage beats 66.83 % of python3 submissions.
}
*/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        '''if not s or s == '[]': return NestedInteger()
        if s[0] != '[': return NestedInteger(int(s))
        i, level, output = 1, 0, NestedInteger()
        for j, c in enumerate(s):
            if level == 1 and (c == ',' or j == len(s) - 1):
                output.add(self.deserialize(s[i:j]))
                i = j + 1
            if c == '[':
                level += 1
            elif c == ']':
                level -= 1
        return output'''
        
        stack = []
        integerStr = ''
        
        for c in s:
            if c == '[':
                stack.append(NestedInteger())
            elif c == ']':
                if len(integerStr)>0:
                    stack[-1].add(NestedInteger(int(integerStr)))
                integerStr = ''
                poppedList = stack.pop()
                
                if len(stack)==0:
                    return poppedList
                stack[-1].add(poppedList)
            elif c == ',':
                if len(integerStr)>0:
                    stack[-1].add(NestedInteger(int(integerStr)))
                integerStr = ''
            else:
                integerStr += c
        return NestedInteger(int(s))
        
        '''c = eval(s)
        print(type(c))
        if not c or c == []:
            return NestedInteger()
        elif type(c) == int:
            return NestedInteger(c)
        elif type(c) == list:
            for i in c:
                if type(i) == list:
                    
            return 
        print(c)
        return c'''
        