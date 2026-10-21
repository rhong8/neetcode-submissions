class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n-1): return False

        #property: traversing from any node should be able to access all nodes in the tree. 

        # n nodes, n - 1 edges <->  no cycle <-> no disconnected components
        adjSet = defaultdict(set)
        
        for a,b in edges:
            adjSet[a].add(b)
            adjSet[b].add(a)
        
        print(adjSet)


        seen = set()
        

        cycle = False
        
        def dfs(val, mostRecent):
            print(f"exploring {val}")
            #cycle detected
            if val in seen:
                nonlocal cycle
                cycle = True
                return
            
            seen.add(val)
            #dead end.
            if len(adjSet[val]) == 1:
                (element,) = adjSet[val]
                if element == mostRecent:
                    return

            for node in adjSet[val]:
                if node != mostRecent:
                    dfs(node, val)
            
        dfs(0, -1)
        print(f"seen: {seen}")
            
        if cycle: 
            return False 
        else: 
            return len(seen) == n

        #property of trees: it has exactly n-1 edges