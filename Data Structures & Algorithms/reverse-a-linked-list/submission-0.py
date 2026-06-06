# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr != None:
            if curr.next == None:
                head = curr
            
            temp = curr.next #storing the next so we can jump
            curr.next = prev
            prev = curr #setting the previous null to current
            curr = temp #jumping ahead
        #now we need to return the head
        return head