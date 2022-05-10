/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 55.55 %
    Runtime : 32 ms
    Memory Usage : 14.1 MB
    Testcase : 60 / 60 passed
    Ranking : 
        Your runtime beats 85.59 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)
        
        
        
    '''def find(self,num):
        if num != num return 0
        self.find()'''