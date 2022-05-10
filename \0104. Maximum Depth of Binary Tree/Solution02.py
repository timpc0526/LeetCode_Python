/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 71.89 %
    Runtime : 44 ms
    Memory Usage : 16.1 MB
    Testcase : 39 / 39 passed
    Ranking : 
        Your runtime beats 84.46 % of python3 submissions.
        Your memory usage beats 76.46 % of python3 submissions.
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
        self.depth = 0
    def maxDepth(self, root) -> int:
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        self.d = max(left,right)
        return self.d+1
        
    
        
        
        