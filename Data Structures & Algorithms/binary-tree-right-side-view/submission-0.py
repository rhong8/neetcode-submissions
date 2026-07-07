from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #the nodes that are visible from the right side of a tree


        #essentially a bfs, where  nodes are viewable on the right side

        #what if three's multiple node on the same level?

        #it's asking for the rightmost node on each level
        result = []
        if root == None:
            return result
        q = deque()

        q.append(root)

        
        while q:
            for i in range(len(q)):
                node = q.pop()
                if i == 0:
                    result.append(node.val)
                
                if node.right:
                    q.appendleft(node.right)
                if node.left:
                    q.appendleft(node.left)

        




        
        return result