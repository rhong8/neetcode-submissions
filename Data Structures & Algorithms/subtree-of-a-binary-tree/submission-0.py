# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        string_root = []
        string_subroot = []

        def preorder(curr, string) -> str:
            if not curr:
                string.append('n')
                return
            string.append('#')
            string.append(str(curr.val))
            preorder(curr.left, string)
            preorder(curr.right, string)


        preorder(root, string_root)
        preorder(subRoot, string_subroot)

        string_root = ''.join(string_root)
        print(string_root)
        string_subroot = ''.join(string_subroot)
        print(string_subroot)


        return string_subroot in string_root

        