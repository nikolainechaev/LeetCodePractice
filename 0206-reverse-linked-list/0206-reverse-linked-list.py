class Solution:
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            nextStep = current.next
            current.next = prev
            prev = current
            current = nextStep
        return prev