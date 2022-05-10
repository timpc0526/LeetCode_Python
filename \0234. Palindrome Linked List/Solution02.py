/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 46.68 %
    Runtime : 1120 ms
    Memory Usage : 46.8 MB
    Testcase : 86 / 86 passed
    Ranking : 
        Your runtime beats 36.34 % of python3 submissions.
        Your memory usage beats 37.58 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # 1148ms ft34.68
        h = head
        hl = []
        while(h):
            hl.append(h.val)
            h = h.next
        
        for i in range(len(hl)//2):
            if hl[i] != hl[-(i+1)]:
                return False
        return True