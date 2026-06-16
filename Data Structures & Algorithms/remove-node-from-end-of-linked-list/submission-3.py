# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #solution with dummy node
        dummy = ListNode(0, head)
        curr = dummy
        dummy.next = head
        ahead = head
        count = 0
        while count < n:
            ahead = ahead.next #increment ahead
            count += 1

    

        while ahead:
            ahead = ahead.next
            curr = curr.next
        
        
        
        #now curr should be directly behind the node we want to remove
        curr.next = curr.next.next

        return dummy.next

