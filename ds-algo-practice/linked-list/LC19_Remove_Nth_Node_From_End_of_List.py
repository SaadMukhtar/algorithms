# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        dummy = ListNode(0, next=head)
        curr, prev = head, dummy
        i = 1
        while i != (length+1-n):
            prev = curr
            curr = curr.next
            i += 1
        prev.next = curr.next
        return dummy.next