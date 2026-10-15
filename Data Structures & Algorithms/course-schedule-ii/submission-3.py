class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Edge course -> prereq, so DFS walks toward prerequisites
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        UNVISITED, ON_PATH, DONE = 0, 1, 2
        state = [UNVISITED] * numCourses
        res = []

        # Returns True if a cycle is found
        def dfs(node):
            state[node] = ON_PATH
            for nxt in adj[node]:
                if state[nxt] == ON_PATH:
                    return True              # back edge -> cycle
                if state[nxt] == UNVISITED and dfs(nxt):
                    return True              # propagate cycle upward
                # DONE: subtree already in res, skip
            state[node] = DONE
            res.append(node)                 # post-order: all prereqs already appended
            return False

        for c in range(numCourses):
            if state[c] == UNVISITED and dfs(c):
                return []
        return res