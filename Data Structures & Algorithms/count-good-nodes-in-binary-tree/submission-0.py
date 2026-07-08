# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(root, greatest):
            if root == None:
                return 0
            
            if root.val >= greatest:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return dfs(root.left, greatest) + dfs(root.right, greatest)
            
        

        #the first node must be good, so our greatest at that point is -infinity to ensure it will be counted.
        return dfs(root, root.val)