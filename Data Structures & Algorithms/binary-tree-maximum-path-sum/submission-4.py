# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = root.val
     

        def postorder(node):
            if not node:
                return 0
            
            val_left = postorder(node.left)

            val_right = postorder(node.right)

           
            
            local_sum = val_left + val_right + node.val
            print(f"local sum is {local_sum}: {val_left} + {val_right} + {node.val}")
            self.max_path_sum = max(self.max_path_sum, local_sum)
            
            larger = max(val_left, val_right) + node.val
            if larger < 0: larger = 0
            print(f"The larger is {larger}")

            return larger


        
        print(postorder(root))



        return self.max_path_sum