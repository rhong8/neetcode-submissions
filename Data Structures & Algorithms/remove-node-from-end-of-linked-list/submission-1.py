# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr, ahead = head, head

        #have ahead go n spaces ahead.then while ahead is not null, increment
        #it until it reaches null. Then curr will be at the desired position and prev can re-link

        count = 0
        while count < n:
            ahead = ahead.next
            count +=1
        print(ahead != None)
        while ahead:
            print("i'm running")
            ahead = ahead.next
            prev = curr
            curr = curr.next 

         #if the nodes moved at all
        if prev:
            prev.next = curr.next
        else: #it didn't move, then set head to null
            head = head.next

        
        return head
        
        
        
       