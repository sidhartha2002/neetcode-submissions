# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # dummy node
        tail = dummy # assigning the dummy linkedNode here...

        while list1 and list2: # while both nodes are non-null
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next # else tail will points to it next node addrs.
        
        if list1: # if list1 node is not null update the tail next pointer to this.
            tail.next = list1
        else: # if list2 node is not null update the tail next pointer to this
            tail.next = list2
        
        return dummy.next


