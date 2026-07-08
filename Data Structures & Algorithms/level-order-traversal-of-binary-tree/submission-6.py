from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        q = deque()

        q.appendleft(root)

        while q:
            inner_list = []
            for _ in range(len(q)):
                node = q.pop()
                if node:
                    inner_list.append(node.val)
                    if node.left:
                        q.appendleft(node.left)
                    if node.right:
                        q.appendleft(node.right)
            
            if inner_list:
                result.append(inner_list)



        return result