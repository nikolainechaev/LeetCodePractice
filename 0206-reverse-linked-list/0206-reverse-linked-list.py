class Solution:
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            following = current.next
            current.next = prev
            prev = current
            current = following
        return prev
            