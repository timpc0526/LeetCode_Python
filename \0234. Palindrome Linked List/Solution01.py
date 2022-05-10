/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 46.68 %
    Runtime : 884 ms
    Memory Usage : 46.6 MB
    Testcase : 86 / 86 passed
    Ranking : 
        Your runtime beats 72.79 % of python3 submissions.
        Your memory usage beats 47.25 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        h = head
        hl = []
        while(h):
            hl.append(h.val)
            h = h.next
        if hl == hl[::-1]:
            return True
        else:
            return False
        
        # 1120ms ft37.51
        '''h = head
        hl = []
        while(h):
            hl.append(h.val)
            h = h.next
        
        for i in range(len(hl)//2):
            if hl[i] != hl[-(i+1)]:
                return False
        return True'''