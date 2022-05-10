/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 70.33 %
    Runtime : 49 ms
    Memory Usage : 16.2 MB
    Testcase : 28 / 28 passed
    Ranking : 
        Your runtime beats 50.61 % of python3 submissions.
        Your memory usage beats 24.42 % of python3 submissions.
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
        hlen = 0
        hl = []
        while(h):
            hlen += 1
            hl.append(h.val)
            h = h.next
        hl.reverse()
        for i in hl:
            a.next = ListNode(i)
            a = a.next
        return b.next