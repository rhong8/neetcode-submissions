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
        if root == None:
            return result
        q = deque()

        q.append((root, 0)) #We append a tuple of the node and the level its currently on
        level = 0

        
        

        while len(q) > 0:

            inner_list = []
            print("queue: ", q)

            while len(q) > 0 and level == q[-1][1]: #while the level is equal to the level indicator
                node = q.pop()
                
                #Only append if it's not None


                
                if node[0].left != None:
                    q.appendleft((node[0].left, node[1] + 1))
                if node[0].right != None:
                    q.appendleft((node[0].right, node[1] + 1))

                print("adding ", node[0].val)
                inner_list.append(node[0].val)
            
            
            level += 1
            print(f"innerlist: {inner_list}")
            result.append(inner_list)



        print("final queue" , q)
        return result