# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(N) and O(1)
        # curr = head
        # prev = None
        # while(curr):
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev
        
        # Recursively - O(N) and O(N)
        
        if not head:
            return None
        newHead = head
        if head.next:
            self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead