/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 60.35 %
    Runtime : 100 ms
    Memory Usage : 30.5 MB
    Testcase : 208 / 208 passed
    Ranking : 
        Your runtime beats 00.00 % of submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import numpy as np
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []
        
        while l1:
            s1 += [l1.val]
            l1 = l1.next
        
        while l2:
            s2 += [l2.val]
            l2 = l2.next
        
        s = sorted(s1+s2)  #merge and sort the combined list
        
        point = head = ListNode(0)
        for k in s:
            point.next = ListNode(k)
            point = point.next
        return head.next
    
    
        '''self.hihi = []
        self.ans(l1,l2)
    def ans(self,a,b):
        #print(a.val)
        #print(b.val)
        if a != None:
            self.hihi.append(a.val)
        if b != None:
            self.hihi.append(b.val)
        if a == None and b == None:
            return (self.hihi)
            print(self.hihi)
        self.ans(a.next,b.next)
    def find(self,num):
        if num.val == None:
            return 0
        self.hihi.append(num.val)
        self.find(num.next)'''
        