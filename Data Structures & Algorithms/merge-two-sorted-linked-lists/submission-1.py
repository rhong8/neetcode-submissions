# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2
        dummy = ListNode(0)
        curr3 = dummy

        while curr1 is not None or curr2 is not None:
            #both valid
            if curr1 is not None and curr2 is not None:
                if curr1.val <= curr2.val:
                    node = ListNode(curr1.val)
                    curr1 = curr1.next
                else: #curr2's val is bigger
                    node = ListNode(curr2.val)
                    curr2 = curr2.next
            elif curr1 is not None: #curr1 is valid, curr2 isn't
                node = ListNode(curr1.val)
                curr1 = curr1.next
            else: #curr2 is valid, curr1 isn't
                node = ListNode(curr2.val)
                curr2 = curr2.next
            curr3.next = node
            curr3 = curr3.next

        return dummy.next


