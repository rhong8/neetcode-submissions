# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string_root = []
        
        def preorder(curr, string) -> str:
            string.append('#')
            if not curr:
                string.append('n')
                return
            '''
            if not curr.left and not curr.right:
                string.append("N")
            '''
            
            string.append(str(curr.val))
            preorder(curr.left, string)
            preorder(curr.right, string)


        preorder(root, string_root)
        
        string = ''.join(string_root[1:])
        print(string)
        return string


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        stack = []
        stack.append(data[0]) # the first element

        vals = iter(data.split('#'))
        

        def build():
            val = next(vals) #next value of preorder traversal
            if val == 'n':
                return None
            
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        
        return build()
        
        
       