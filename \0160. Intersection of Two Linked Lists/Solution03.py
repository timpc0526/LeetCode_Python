/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 49.99 %
    Runtime : 260 ms
    Memory Usage : 29.5 MB
    Testcase : 39 / 39 passed
    Ranking : 
        Your runtime beats 21.83 % of python3 submissions.
        Your memory usage beats 70.96 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 203ms ft50.68
        a, b = headA, headB
        while a != b:
            if not a:
                a = headB
            elif not b:
                b = headA
            else:
                a = a.next
                b = b.next
        return a
        
        # 18ms ft74.18
        '''nodeA, nodeB = headA, headB
        while nodeA is not nodeB:
            nodeA = headB if not nodeA else nodeA.next
            nodeB = headA if not nodeB else nodeB.next
            #print(nodeA)
            #print(nodeB)
        return nodeA'''