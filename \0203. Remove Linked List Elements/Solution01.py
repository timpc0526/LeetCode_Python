/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 43.52 %
    Runtime : 84 ms
    Memory Usage : 17.9 MB
    Testcase : 66 / 66 passed
    Ranking : 
        Your runtime beats 60.62 % of python3 submissions.
        Your memory usage beats 36.77 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
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