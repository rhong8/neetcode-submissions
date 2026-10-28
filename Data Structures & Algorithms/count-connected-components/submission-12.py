class TreeNode:
    def __init__(self, value):
        self.parent = None
        self.value = value
        self.children = []

    def add_child(self, node):
        node.parent = self
        
        self.children.append(node)

    def find_root(self, node, x):
        if self.parent is None:
            return self
        
        return self.find_root(self.parent, self.parent.value)

    def find_root(self):
        
        node = self
        if node.parent is None:
            return node
        
        
        while node.parent:
            node = node.parent #go up the parent chain
        return node
    
    def dfs_print(self, node):
        if not node:
            return

        #print(node.value)
        for c in node.children:
            self.dfs_print(c)


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        forest = set()
        nodes = [None] * n
        #[0,1]
        #[1,2]
        #logic: utilize a dictionary of the nodes
        # if the node exists , simply add to its children
        # doesn't exist yet? we have a new group.

        #case: union: when you have an edge
        # [0,1] [1,2] [3,4] [2,3] for example.  you set the parent of that to one of them.
        # 
        for a,b in edges:
            #print(f"Run {a,b}")
            if nodes[a] is None and nodes[b] is None:
                #print("Both havent been initalized")
                tn_a = TreeNode(a)
                tn_b = TreeNode(b)
                tn_a.add_child(tn_b)
                
                forest.add(tn_a) #forest contains the roots of all the trees
                nodes[a] = tn_a
                nodes[b] = tn_b
            elif nodes[a] is not None and nodes[b] is None: #a has been initialized, but not b
                #print(f"{a} has been initialized but not {b}")
                tn_b = TreeNode(b)
                nodes[a].add_child(tn_b)
                nodes[b] = tn_b
                
            elif nodes[b] is not None and nodes[a] is None: #b has been initialized but not a
                #print(f"{b} has been initialized but not {a}")
                tn_a = TreeNode(a)
                nodes[b].add_child(tn_a)
                nodes[a] = tn_a


            else: 
                print("both exist.")
                
                tn_a = nodes[a]
                tn_b = nodes[b]

                root_a = tn_a.find_root()
                root_b = tn_b.find_root()

                #print(f"root values: a: {a} b: {b}")


                #only if they share distinct parents
                if root_a != root_b:
                #b is now part of tree of root A. b is gone from the forest.
                    root_a.add_child(root_b)
                    forest.remove(root_b) 
            
            #print("Forest: ")
            
            for t in forest:
                #print("Tree:")
                t.dfs_print(t)
            

        
        #print(f"Forest: {forest}")
        '''
        for root in forest:
            print(root.value)
        '''
        #print(f"Nodes: {nodes}")

        #print("Forest: ")
        for t in forest:
            t.dfs_print(t)

        count = 0

        for n in nodes:
            if not n:
                count += 1
        count += len(forest)

        return count
        















    