# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2

        dummy = ListNode(0)
        curr3 = dummy


        #returns the sum of ptr1's val, ptr2's val, and the sum of the carry, checking if they are valid
        def get_sum(ptr1, ptr2, carry):
            sum = 0
            if ptr1 is not None:
                sum += ptr1.val
            if ptr2 is not None:
                sum += ptr2.val
            
            return sum + carry
            
        

        carry = 0
        count = 0
        while curr1 or curr2:
            sum = get_sum(curr1, curr2, carry)
            print(f"iteration sum {sum} carry {carry} count {count}")
            

            if sum >= 10:
                sum = sum - 10
                carry = 1
            else:
                carry = 0
            

            if curr1 and curr2: #both pointers are valid here  
                curr3.next = ListNode(sum)
                print(curr3.val)
                curr1 = curr1.next
                curr2 = curr2.next
                
            elif curr1:
                curr3.next = ListNode(sum)
                curr1 = curr1.next
                
                
            else:
                curr3.next = ListNode(sum)
                curr2 = curr2.next
            
            curr3 = curr3.next
            
            
        if carry != 0:
            curr3.next = ListNode(1)

        
        
        

        return dummy.next