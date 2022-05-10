/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 70.33 %
    Runtime : 57 ms
    Memory Usage : 15.4 MB
    Testcase : 28 / 28 passed
    Ranking : 
        Your runtime beats 32.94 % of python3 submissions.
        Your memory usage beats 56.83 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #48ms ft49.64
        new_head = None
        while head:
            node = head.next
            head.next = new_head
            new_head = head
            head = node
        return new_head
        
        # 49ms ft48
        '''b = ListNode(0)
        a = b
        h = head
        hl = []
        while(h):
            hl.append(h.val)
            h = h.next
        hl.reverse()
        for i in hl:
            a.next = ListNode(i)
            a = a.next
        return b.next'''