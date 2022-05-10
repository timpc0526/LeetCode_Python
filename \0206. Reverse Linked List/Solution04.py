/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 70.33 %
    Runtime : 67 ms
    Memory Usage : 16.3 MB
    Testcase : 28 / 28 passed
    Ranking : 
        Your runtime beats 16.16 % of python3 submissions.
        Your memory usage beats 19.77 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        b = ListNode(0)
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
        return b.next