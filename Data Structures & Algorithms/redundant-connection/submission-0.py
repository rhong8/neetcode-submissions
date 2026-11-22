from collections import deque


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [0] * (len(edges))
        rank = [0] * (len(edges))
        for i in range(len(edges)):
            parent[i] = i
        

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] #make the parent search faster. but why?
                x = parent[x]

            return x
        
        print(parent)
        
        for u,v in edges:
            ra = find(u-1)
            rb = find(v-1)
            print(ra)

            print(rb)

            if ra == rb:
                return [u,v]
            elif rank[ra] < rank[rb]:
                #set parent
                parent[ra] = parent[rb]
            elif rank[rb] < rank[ra]:
                parent[rb] = parent[ra]
            else:
                rank[ra] += 1
                parent[rb] = ra

        




        return [0]