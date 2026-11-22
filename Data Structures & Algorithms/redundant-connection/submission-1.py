class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [0] * (len(edges))
        rank = [0] * len(edges)

        for i in range(len(edges)):
            parent[i] = i
        
        print(parent)
        

        def find(x):
            print(f"tryna find {x}")
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        

        for u,v in edges:
            ra = find(u-1)
            rb = find(v-1)

            #same tree
            if ra == rb:
                return [u,v]
            elif rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[rb] < rank[ra]:
                parent[rb] = ra
            else:
                rank[ra] += 1
                parent[rb] = ra
        

        return edges[-1]