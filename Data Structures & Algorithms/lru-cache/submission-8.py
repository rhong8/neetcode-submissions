class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        #Two dummy nodes at the side named left and right
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = defaultdict(None)
        

    #remove a node from the list, could be anywhere
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        

    #insert at the end of the list
    def insert(self, node):
        right, prev = self.right, self.right.prev
        prev.next = right.prev = node
        node.prev = prev
        node.next = right

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None: 
        #if it already exists in the list, then remove it.
        if key in self.cache:
            self.remove(self.cache[key])
        #insert the node with the new k-v pair
        new_node = Node(key,value)
        self.insert(new_node)
        self.cache[key] = new_node

        
        #if it's past its capacity: Remove the lru
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        
        



        
