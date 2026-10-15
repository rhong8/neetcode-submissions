class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjSet = defaultdict(set)
        visited = set()
        #maps a course to its requirements
        res = True
        for a,b in prerequisites: 
            adjSet[b].add(a)
        
        #print(f"adjset 1: {adjSet}")

        def dfs(val, origins):
            #print(f"exploring {val}")
            #base case: we have already explored the entire tree
            #base case: a value has no prerequisite courses
            if not adjSet[val]: 
                #for num in origins:
                    #print(f"adding {num}")
                    #visited.add(num) #all of these are not part of a chain
                return
            #print(f"Exploring {val}")
            #print(f"courses that depend: {adjSet[val]} my origin is {origin}")
            #print(f"Is the origin in the depend? {origin in adjSet[val]}")

            #intersection
            #print(f"origins: {origins}")
            #print(f"adjSet[val]: {adjSet[val]}")
            #print(f"intersection: {origins.intersection(adjSet[val])}")
            if origins.intersection(adjSet[val]):
                nonlocal res
                res = False
                #print("RES RESULT IS NOW" , res)
                return
                
            for num in adjSet[val]:
                #pick up that seen value and keep traversing dfs
                if num not in visited:  
                    origins.add(num)
                    dfs(num, origins)
                    origins.remove(num)
            visited.add(val)
                
        #print(f"adjset 2: {adjSet}")
        for num in list(adjSet.keys()):
            #print(f"num: {num}")
            #print(len(adjSet))
            
            start = set()
            start.add(num)
            if num not in visited:
                dfs(num, start)
            if res == False: return False
        #print(res)
        return True