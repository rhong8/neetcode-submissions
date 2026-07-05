# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True

        #Preorder Traversal
        def dfs(curr1, curr2):
            
            if not curr1 and not curr2: 
                return

            if curr1:
                print(f"curr1: {curr1.val}")
            else:
                print("curr1 is null")
            if curr2:
                print(f"curr2: {curr2.val}")
            else:
                print("curr2 is null")
        
            #If one of them is None, and the other one isn't, or they have mismatching values
            if (curr1 == None) or (curr2 == None) or (curr1.val != curr2.val):
                
                self.same = False
                return

            print(curr1.left, curr2.left)
            print(curr1.right, curr2.right)
            dfs(curr1.left, curr2.left)
            dfs(curr1.right, curr2.right)
        

        dfs(p,q)

        return self.same
            
