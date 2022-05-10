/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 43.52 %
    Runtime : 130 ms
    Memory Usage : 17.3 MB
    Testcase : 66 / 66 passed
    Ranking : 
        Your runtime beats 11.68 % of python3 submissions.
        Your memory usage beats 92.93 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # 91ms ft47.28
        if head == None:
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
            return head