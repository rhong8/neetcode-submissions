class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        
        #Graph valid tree with Union Find strat

        parent = [0] * n
        rank = [0] * n

        def find(x):
            print(f"finding {x}")
            while x != parent[x]:
                #set its parent to its grandparent
                parent[x] = parent[parent[x]]
                x = parent[x] #go to its new parent (used to be grandparent)
                print(f"going to my parent: {x}")

            return x
        
        #build the tree as you go?
        for i in range(n):
            parent[i] = i
        
        print(parent)

        for u,v in edges:
            ru = find(u) #root of u
            rv = find(v) #root of v

            print(f"root of {u} is {ru}. rank is {rank[ru]}")
            print(f"root of {v} is {rv}, rank is {rank[rv]}")

            if ru == rv:
                return False
            elif rank[ru] < rank[rv]: 
                print("")
                #ru has a smaller rank
                #rv should be the parent
                parent[ru] = rv
            elif rank[rv] < rank[ru]:
                parent[rv] = ru
            else:
                #the ranks are equal
                rank[ru] += 1
                parent[rv] = ru
        
        return True
