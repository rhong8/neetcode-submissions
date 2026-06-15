# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #find the midpoint
            
        prev = None  
        flipper = slow.next #the node after the midpoint

        slow.next = None #sever the midpoint


        flipperHead = None
        while flipper != None:
            if flipper.next == None:
                flipperHead = flipper
            temp = flipper.next
            flipper.next = prev #rewrire
            prev = flipper #move previous to flipper
            flipper = temp #increment to the next
            

        #"thread the needle between the two lists"
        curr1 = head #0
        curr2 = flipperHead #2

        while curr2: #neither of them is null
            temp = curr1.next 
            temp2 = curr2.next

            curr1.next = curr2
            

            curr1 = temp #increment curr1
            curr2.next = temp #BACK TO 1
            curr2 = temp2 #increment curr2
                #needs to connect back to curr1


