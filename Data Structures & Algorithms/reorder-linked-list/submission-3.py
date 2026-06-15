# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #so the middle pointer is slow

        second = slow.next #This is the second half
        prev = None
        slow.next = None #sever the connection

        #reverse second half of the list
        while second:
            temp = second.next
            second.next = prev #rewire backwards
            prev = second #update prev
            second = temp #increment the list forward
        

        #prev is the head of the second list. merge the two halves
        curr1 = head
        curr2 = prev 

        while curr2:
            temp1 = curr1.next
            temp2 = curr2.next 
            curr1.next = curr2
           
            curr1 = temp1 #increment curr1 forward
            curr2.next = temp1 #link curr2 to curr1

            curr2 = temp2 #increment curr2 forward
            
        
            