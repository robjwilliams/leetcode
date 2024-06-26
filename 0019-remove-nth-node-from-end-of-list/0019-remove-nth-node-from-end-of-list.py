# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        slow = fast = head
        prev = None
        
        for _ in range(n):
            fast = fast.next
        
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        if prev:
            prev.next = slow.next
        else:
            head = slow.next
        return head
        