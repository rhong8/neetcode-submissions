# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        local_min_ptr = None
        dummy = ListNode(0, None)
        tail = dummy
        result = []



        def atLeastOneNode(lists: List[Optional[ListNode]]):
            for p in lists:

                
                if p is not None:
                    #print("Found a non-null")
                    return True
            return False



        while atLeastOneNode(lists):
            local_min = float('inf')
            local_min_i = -1
            for idx, ptr in enumerate(lists):
                #find the node with the smallest val
                if ptr and ptr.val < local_min: #smaller than loacal min
                    #local_min_ptr = ptr
                    local_min = ptr.val
                    local_min_i = idx
            
            print(f"We have our minimum: it's at index {local_min_i} and value {local_min}")
            #tail.next = local_min_ptr
            tail.next = lists[local_min_i]

            lists[local_min_i] = lists[local_min_i].next
            #local_min_ptr = local_min_ptr.next
            tail = tail.next


        return dummy.next