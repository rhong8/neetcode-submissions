"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0, None, None)
        curr = dummy
        listptr = head
        #Two pass solution  
        #Key: pointer in the given list Value: pointer in the copied list
        pointers_dict = dict() 


        #establish the next pointers first
        while listptr:
            new_node = Node(listptr.val, None, None)
            
            pointers_dict[listptr] = new_node

            curr.next = new_node
            
            curr = curr.next
            #print(f"curr.val: {curr.val}")
            listptr = listptr.next

            #print(f"tacking on new_node: {new_node.val}")
        


        listptr = head #set it to head again
        curr = dummy.next #bring curr to dummy again, this time going through and setting random

        count = 0
        while listptr:
            #print(f"i'm iterating {count}")
            #map to that pointer
            
            deep_random_ptr = pointers_dict.get(listptr.random)
                
            #if curr == None: print ("curr is none bro.")
            curr.random = deep_random_ptr
            curr = curr.next
            listptr = listptr.next
            count += 1


        return dummy.next