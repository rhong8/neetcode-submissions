# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #Canonical Solution

        def valid(root, lower, upper):
            if not root:
                return True
            
            if not lower < root.val < upper:
                return False
            
            return valid(root.left, lower, root.val) and valid(root.right, root.val, upper)
        

        return valid(root, float("-inf"), float("inf"))