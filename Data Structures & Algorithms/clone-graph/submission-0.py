from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        seen = dict() #old node to - new_node
        q = deque()
        q.append(node)
        seen[node] = Node(node.val) 

        while q:
            cur = q.popleft() #this is our old node right here
            #link up the neighbors
            for neigh in cur.neighbors:
                if neigh not in seen:
                    new_node = Node(neigh.val)
                    seen[neigh] = new_node
                    q.append(neigh)
                else:
                    new_node = seen[neigh]
                seen[cur].neighbors.append(new_node)
                


        return seen[node]
