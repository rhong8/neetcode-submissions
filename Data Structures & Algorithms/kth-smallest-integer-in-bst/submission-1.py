# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Iterative Solution
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        #condition n ==k :
        cur = root


        while cur or stack:
            print("i'm entering the loop")
            while cur: #run till it's null
                stack.append(cur)
                cur = cur.left
            print(cur is not None)
            cur = stack.pop() #process it
            n += 1

            if n == k:
                return cur.val
            cur = cur.right #move it to the right, it's going to the run the loop again
        
        
        return cur.val