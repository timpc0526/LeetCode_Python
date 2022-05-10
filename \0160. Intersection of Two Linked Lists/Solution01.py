/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 49.99 %
    Runtime : 305 ms
    Memory Usage : 29.5 MB
    Testcase : 39 / 39 passed
    Ranking : 
        Your runtime beats 7.88 % of python3 submissions.
        Your memory usage beats 94.85 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        alen, blen = 0, 0
        while(a):
            alen+=1
            a = a.next
        while(b):
            blen+=1
            b = b.next
            
        while alen > blen:
            headA = headA.next
            alen-=1
        while blen > alen:
            headB = headB.next
            blen-=1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
        
        
        # 203ms ft50.68
        '''a, b = headA, headB
        while a != b:
            if not a:
                a = headB
            elif not b:
                b = headA
            else:
                a = a.next
                b = b.next
        return a'''
        
        # 18ms ft74.18
        '''nodeA, nodeB = headA, headB
        while nodeA is not nodeB:
            nodeA = headB if not nodeA else nodeA.next
            nodeB = headA if not nodeB else nodeB.next
            #print(nodeA)
            #print(nodeB)
        return nodeA'''