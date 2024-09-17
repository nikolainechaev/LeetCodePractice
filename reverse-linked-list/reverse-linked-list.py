class Solution:
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        
        while current:
            nextNode = current.next
            
            current.next = prev
            prev = current
            current = nextNode
        return prev