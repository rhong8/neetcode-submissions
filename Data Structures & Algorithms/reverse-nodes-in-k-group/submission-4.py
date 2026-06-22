# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        saved_head = None
        local_head = None
        scout = curr = head
        prev = None
        linker = None
        prev_linker = None
        scout_i = 0

        while curr:

            #start of the group
            scout_i = 0
            while scout and scout_i < k:
                scout = scout.next
                scout_i += 1
            if scout_i < k:
                if prev_linker:
                    prev_linker.next = curr #connect the rest of the list
                return saved_head
            
            linker = curr #pit's the first node of each group, where curr is at

            #reset prev to None, because the last node of each group should point to none for now
            prev = None 
            while curr != scout: #run the reverse algorithm
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            if prev_linker:
                prev_linker.next = prev
        
            if saved_head is None: #the head of the entire list is the last node of the first group
                saved_head = prev
            


            prev_linker = linker

            #done reversing the first section.
            #set linker's next to curr
            
            print(f"linker: {linker.val} curr: {curr.val if curr else 'None'}")
            print(f"prev: {prev.val}")
            
            #how do we set the linker to the head of the next one?
            #linker.next = curr #this skips all the other nodes.. how do we see into the future, per se? should i use a stack?
            #placeholder


            print("printing list:")
            ptr = saved_head

            while ptr:
                print(ptr.val, end = " ")
                ptr = ptr.next
            print("")
            
        
        return saved_head

            

