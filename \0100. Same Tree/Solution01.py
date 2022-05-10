/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 55.55 %
    Runtime : 20 ms
    Memory Usage : 14.2 MB
    Testcase : 60 / 60 passed
    Ranking : 
        Your runtime beats 99.70 % of python3 submissions.
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
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        right = self.isSameTree(p.right,q.right)
        left = self.isSameTree(p.left,q.left)
        return right and left
        
        
        
    '''def find(self,num):
        if num != num return 0
        self.find()'''