/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 71.89 %
    Runtime : 40 ms
    Memory Usage : 16.2 MB
    Testcase : 39 / 39 passed
    Ranking : 
        Your runtime beats 93.33 % of python3 submissions.
        Your memory usage beats 75.16 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        pass
    def maxDepth(self, root) -> int:
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        d = max(left,right)
        return d+1
        
    
        
        
        