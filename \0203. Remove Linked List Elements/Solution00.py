/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 43.52 %
    Runtime : 68 ms
    Memory Usage : 17.7 MB
    Testcase : 66 / 66 passed
    Ranking : 
        Your runtime beats 93.28 % of python3 submissions.
        Your memory usage beats 81.35 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 84ms ft53.85
        a = ListNode(0)
        a.next = head
        h = a
        while(h.next):
            if h.next.val == val:
                h.next = h.next.next
            else:
                h = h.next
        return a.next
        
        

        # 91ms ft47.28
        '''if head == None:
            return head
        h = head
        while(h.next):
            if h.next.val == val:
                h.next = h.next.next
            else:
                h = h.next
        if head.val == val:
            return head.next
        else:
            return head'''