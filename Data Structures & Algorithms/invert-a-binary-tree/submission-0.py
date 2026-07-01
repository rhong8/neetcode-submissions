# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        stack = []
        stack.append(root)
        

        while len(stack) > 0:
            current = stack.pop()

            if current != None:
                temp = current.left
                current.left = current.right
                current.right = temp
                stack.append(current.left)
                stack.append(current.right)
        

        return root

