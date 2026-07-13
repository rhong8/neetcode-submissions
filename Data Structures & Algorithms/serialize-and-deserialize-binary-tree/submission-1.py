# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def preorder(node):
            if not node:
                result.append('n')
                return
            result.append(str(node.val))

            preorder(node.left)
            preorder(node.right)

        preorder(root)

        string = ','.join(result)
        print(string)
        return string


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #Make an iterator


        vals = iter(data.split(','))

        def build():
            val = next(vals)
            if val == 'n':
                return None
            
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()

            return node
        

        return build()
