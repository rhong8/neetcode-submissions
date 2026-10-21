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
        def dfs(curr):
            seen.add(curr)
            for node in adjList[curr]:
                if node not in seen:
                    dfs(node)
        
        dfs(0)
        
        return len(seen) == n