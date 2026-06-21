from collections import defaultdict
class LRUCache:
    class ListNode:
        def __init__(self, val=0, next=None, prev=None):
            self.val = val
            self.next = next
            self.prev = prev

    def _print_list(self, label=""):
        if label:
            print(f"\n{label}")
        curr = self.head
        nodes = []
        while curr:
            nodes.append(str(curr.val))
            curr = curr.next
        print("HEAD -> " + " <-> ".join(nodes) + " <- TAIL")

    def __init__(self, capacity: int):
        self.pointers_dict = defaultdict(lambda: None)
        self.count = 0
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        ptr = self.pointers_dict[key]
        if ptr is None:
            self._print_list(f"After get({key}) → -1")
            return -1
        value = ptr.val[1]
        if ptr == self.tail: #if it's the tail do nothing
            pass
        elif ptr == self.head: #trim the head
            
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            
            self.tail.next = LRUCache.ListNode(list((key, value)), None, self.tail)
            self.tail = self.tail.next
            self.pointers_dict[key] = self.tail
        else:    #if it's in the middle
            ptr.prev.next = ptr.next
            ptr.next.prev = ptr.prev
            self.tail.next = LRUCache.ListNode(list((key, value)), None, self.tail) #create a new node at the tail
            self.tail = self.tail.next #move tail forward
            self.pointers_dict[key] = self.tail
        self._print_list(f"After get({key}) → {value}")
        return value

    def put(self, key: int, value: int) -> None:
        ptr = self.pointers_dict[key]
        if self.pointers_dict[key] is not None and ptr == self.tail: #it's the tail
            self.pointers_dict[key].val[1] = value
            self._print_list(f"After put({key},{value})")
            return
        elif self.pointers_dict[key] is not None: #exists in the list, and isn't the tail
            if ptr == self.head:
                self.head = self.head.next #trim the head
                self.head.prev = None
                


            else: #in the middle
                ptr.prev.next = ptr.next #remove the node from the middle
                ptr.next.prev = ptr.prev
                     
        else:
            if self.count + 1 > self.capacity:
                for_deletion = self.head.val[0]
                del self.pointers_dict[for_deletion]
                if self.head.next is not None:
                    self.head = self.head.next
                    self.head.prev = None
                else:
                    self.head = None
                    self.tail = None
            else:
                self.count += 1
        
        node = LRUCache.ListNode(list((key, value)), None, self.tail)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.pointers_dict[key] = self.tail
        self._print_list(f"After put({key},{value})")