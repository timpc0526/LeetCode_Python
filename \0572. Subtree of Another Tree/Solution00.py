/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 45.36 %
    Runtime : 68 ms
    Memory Usage : 14.9 MB
    Testcase : 183 / 183 passed
    Ranking : 
        Your runtime beats 99.17 % of python3 submissions.
        Your memory usage beats 87.12 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        tree1 = self.preorder(s)
        tree2 = self.preorder(t)
        return tree2 in tree1 
    def preorder(self, node: TreeNode) ->str: 
        if node is None:
            return 'null'
        return ' '+ str(node.val) + " " + self.preorder(node.left) + self.preorder(node.right) 