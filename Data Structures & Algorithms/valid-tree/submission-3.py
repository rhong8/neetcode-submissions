class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        

        #add to an adjList
        adjList = defaultdict(list)

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        seen = set()
        cycle = False
        #base case:
        def dfs(curr, prev):
            if curr in seen:
                nonlocal cycle
                cycle = True
                return
            seen.add(curr)

            for node in adjList[curr]:
                if node != prev:
                    dfs(node,curr)
        
            
        dfs(0, -1)
        
        if cycle: 
            return False
        else:
            return len(seen) == n