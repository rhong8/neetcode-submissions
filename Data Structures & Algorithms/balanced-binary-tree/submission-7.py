# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root): #returning the entire tree's balanced status and height together
            if not root: 
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balance = (left[0] and right[0]) and (abs(left[1] - right[1]) <= 1)

            return [balance, 1 + max(dfs(root.left)[1], dfs(root.right)[1])]
        

        return dfs(root)[0]